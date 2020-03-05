from django.contrib import admin
from django.utils.html import mark_safe
from . import models

@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
      """ Item Admin Definition"""

      list_display = ("name", "used_by") 
      #여기서 name은 위의 항목들의 공통변수이다. 
      # models에서 추상클래스에서 정의된것임. 그것을 상속받은것은 전부 name을 공용한다.


      def used_by(self, obj):
            return obj.rooms.count()
            #여기서 rooms는 models에서 related_name을 roons로 해준 모든것들(facitities
            # ,amenities, host, room_type, house_rule)을 가리킨다.

#photo를 room에서 넣는 방법  PhotoInline을 이와 같이 만들어주고
# 아래 RoomAdmin에 inlines = (PhotoInline, ) 처럼 넣어준다.         
class PhotoInline(admin.TabularInline):
    model  = models.Photo

# class PhotoInline(admin.StackedInline):
#     model  = models.Photo
#StackedInline은 나열방식만 TabularInline과 다르다

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

      """ Item Admin Definition"""
      inlines = (PhotoInline, )

      fieldsets = (
            ("Basic Info", {"fields" : ("name", "description", "country", "city", "address", "price", "room_type")}),
            ("Times", {"fields" : ("check_in", "check_out","instant_book")}),
            ("More About the Space", {"fields" : ("amenities", "facilities", "house_rules")}),
            ("Spaces", {"fields" : ("beds", "guests","baths")}),
            ("Last Details", {"fields" : ("host",)}),

      )
      # readonly_fields=("bedrooms",)



      list_display = (
          "name",
          "description",
          "country",
          "city",
          "price",
          "address",
          "beds",
          "baths",
          "check_in",
          "check_out",
          "instant_book",
          "count_ammenities",
          "count_photos",
          "total_rating",
      )


      # ordering = ("name","price","beds","baths") #정렬순서 정하기

      list_filter = (
            "instant_book",
            "host__superhost",
            "host__gender",
            "room_type",
            "amenities",
            "city",
            "facilities",
            "house_rules",
            "country",
            )
      #filter bar만들기 위에서 써준 순서대로 filter bar가 생긴다.

      filter_horizontal = ("amenities", "facilities", "house_rules")

      #우측으로 옵션을 선택하는 방법

      raw_id_fields = ("host",)
      #host를 찾을때 id로 보이게하고 검색아이콘을 눌러서 검색하게 할 수 있는 기능(raw_id_fields)

 
      search_fields = ("city", "^host__username")
      #search bar를 만들기 - 위의 경우는 도시와 username 어떤것으로도 search가 가능하다.
      #여기서 좀  헤맬수 있는데 host의 foreignkey로 User에 접근하여 변수에 접근할수 있는데
      #User class에는 username이라는 변수가 없다. 그러나 장고는 users앱에 기본적으로 username을
      #가지고 있다고 볼 수 있다.

      def count_ammenities(self, obj): #여기서 self는 RoomAdmin 클래스 자신이다.

            #그리고 obj는 rooms의 하나의 객체를 받는다.
            # print(obj.amenties.all())
            return obj.amenities.count()
      def count_photos(self, obj):
            return obj.photos.count()

      count_photos.short_description = "Photo Count"

      # count_ammenities.short_description = "hello sexy!"
      #count_ammenities를 다른 이름으로 표기되게 하기.

      #여기서 특정이름을 정하고 그것을 list_filter에 넣고 그것의
      # 반환값을 우리가 원하는 값으로 정할 수 있다 함수를 사용하여.
      #그 특정이름을 가진 함수를 만들어 사용한다.

      # def save_model(self, request, obj, form, change):
      #       print(obj, change, form)
      #       # obj.user = request.user
      #       super().save_model(request, obj, form, change)

      #위 코드는 admin을 좀더 컨트롤 할 수 있는 함수.
      # super()매서드를 불러오는것을 잊지 말라 

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
      """ """
      list_display = ("__str__", "get_thumbnail")

      def get_thumbnail(self, obj):
          #print(obj.file.url)
          return mark_safe(f'<img width = "50px" src="{obj.file.url}" />')
          
          #여기서 obj.file의 dir을 찍어보면 여러클래스가 나온다 그중에서 
          #url클래스를 src에 연결하여 썸네일을 리턴한게 해준코드임. 
          #예) print (dir(obj.file)) - file의 많은 함수들이 나온다. 그 중에서 url을 사용하는것이다. 

      #phto admin에 사진을 썸네일이 나오게 하는 함수구현
      #mark_safe함수는 mark_safe뒤의 값을 html그대로 나오는게 아니고 썸네일이 나와주게 한다. 
      #mark_safe함수를사용하지 않으면 썸네일에 <img width = "50px" src="{obj.file.url}" />
      #이렇게 html코드가 나오게 된다. 

      get_thumbnail.short_description = "Thumbnail"