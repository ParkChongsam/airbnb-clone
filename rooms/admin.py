from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
      """ Item Admin Definition"""
      pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

      """ Item Admin Definition"""

      fieldsets = (
            ("Basic Info", {"fields" : ("name", "description", "country", "address", "price")}),
            ("Times", {"fields" : ("check_in", "check_out","instant_book")}),
            ("More About the Space", {"fields" : ("amenties", "facilities", "house_rules")}),
            ("Spaces", {"fields" : ("beds", "guests","baths")}),

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
      )

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


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
      """ """
      pass
