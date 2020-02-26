from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as users_models

class AbstractItem(core_models.TimeStampModel):
      """ Abstrac Item """

      name = models.CharField(max_length=80)

      class Meta:
            abstract = True
      
      def __str__(self):
            return self.name

class RoomType(AbstractItem):

      """ Room Type Definition """

      class Meta:
            verbose_name = "Room Type"

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
      host = models.ForeignKey(users_models.User, on_delete=models.CASCADE)

      #on_delete=models.CASCADE : user가 삭되되면 user의 모든 정보를 삭제하는 기능
      room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
      amenties = models.ManyToManyField(Amenity)
      facilities = models.ManyToManyField(Facility)
      house_rules = models.ManyToManyField(HouseRule)


      def __str__(self):
            return self.name
                


