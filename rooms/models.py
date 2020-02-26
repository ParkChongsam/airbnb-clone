from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as users_models

class AbstractItem(core_models.TimeStampModel):
      """ Abstrac Item """

      name = models.CharField(max_length=80)

      class Meta:
            abstract = True
      
      def __str__(self):  #__str__함수는 admin에 표기될 이름을 지정하는 것이다. 
            return self.name

class RoomType(AbstractItem):

      """ Room Type Definition """

      class Meta:
            verbose_name = "Room Type"
            ordering = ["name"] #알파벳 순서로 나열 name은 장고에 내장된 변수
            # ordering = ["created"]  #생성된 순서로 나열 - created는 TimeStampModel에 만들어진 변수

class Amenity(AbstractItem):

      """ Amenity Type Definition """
      
      class Meta:
            verbose_name_plural = "Amenities"

class Facility(AbstractItem):

      """ Facility Model Definition """

      class Meta:
            verbose_name_plural = "Facilities"

class HouseRule(AbstractItem):

      class Meta:
            verbose_name = "House Rule"

class Photo(core_models.TimeStampModel):

      caption = models.CharField(max_length=80)
      file = models.ImageField()
      room = models.ForeignKey("Room", on_delete=models.CASCADE)
      #room을 삭제하면 사진도 삭제 되어야함.(on_delete=models.CASCADE)
      #사진을 방과 연결시키는 코드임.

      def __str__(self):
            return self.caption        

class Room(core_models.TimeStampModel):

      """ Room Model Definition """

      name = models.CharField(max_length=140)
      description = models.TextField()
      country = CountryField()
      city = models.CharField(max_length=80)
      price = models.IntegerField()
      address = models.CharField(max_length=140)
      beds = models.IntegerField()
      baths = models.IntegerField()
      guests = models.IntegerField()
      check_in = models.TimeField()
      check_out = models.TimeField()
      instant_book = models.BooleanField(default=False)
      host = models.ForeignKey("users.User", on_delete=models.CASCADE)

      #on_delete=models.CASCADE : user가 삭되되면 user의 모든 정보를 삭제하는 기능
      room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
      amenties = models.ManyToManyField("Amenity", blank=True)
      facilities = models.ManyToManyField("Facility", blank=True)
      house_rules = models.ManyToManyField("HouseRule", blank=True)


      def __str__(self):
            return self.name
                


