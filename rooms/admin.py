from django.contrib import admin
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

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

      """ Item Admin Definition"""

      fieldsets = (
            ("Basic Info", {"fields" : ("name", "description", "country", "address", "price")}),
            ("Times", {"fields" : ("check_in", "check_out","instant_book")}),
            ("More About the Space", {"fields" : ("amenties", "facilities", "house_rules")}),
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
            "amenties",
            "city",
            "facilities",
            "house_rules",
            "country",
            )
      #filter bar만들기 위에서 써준 순서대로 filter bar가 생긴다.

      filter_horizontal = ("amenties", "facilities", "house_rules")

      #우측으로 옵션을 선택하는 방법

 
      search_fields = ("city", "^host__username")
      #search bar를 만들기 - 위의 경우는 도시와 username 어떤것으로도 search가 가능하다.
      #여기서 좀  헤맬수 있는데 host의 foreignkey로 User에 접근하여 변수에 접근할수 있는데
      #User에는 username이라는 변수가 없다. 그러나 장고는 users앱에 기본적으로 username을
      #가지고 있다고 볼 수 있다.

      def count_ammenities(self, obj): #여기서 self는 RoomAdmin 클래스 자신이다.

            #그리고 obj는 rooms의 하나의 객체를 받는다.
            # print(obj.amenties.all())
            return obj.amenties.count()
      def count_photos(self, obj):
            return obj.photos.count()

      count_ammenities.short_description = "hello sexy!"
      #count_ammenities를 다른 이름으로 표기되게 하기.

      #여기서 특정이름을 정하고 그것을 list_filter에 넣고 그것의
      # 반환값을 우리가 원하는 값으로 정할 수 있다 함수를 사용하여.
      #그 특정이름을 가진 함수를 만들어 사용한다.




                    


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
      """ """
      pass
