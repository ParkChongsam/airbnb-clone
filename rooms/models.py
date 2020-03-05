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
      file = models.ImageField(upload_to='room_photos')
      #uploads폴더내에서 room_photos 폴더를 만들어서 거기에 사진을 저장한다.
      room = models.ForeignKey("Room", related_name= "photos", on_delete=models.CASCADE)
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
      # bedr]5ooms = models.IntegerField()
      guests = models.IntegerField()
      check_in = models.TimeField()
      check_out = models.TimeField()
      instant_book = models.BooleanField(default=False)
      host = models.ForeignKey("users.User", related_name = "rooms", on_delete=models.CASCADE)
      #_set을 related_name으로 지정해주면 >>예)park.room_set.all() 아니고
      #park.rooms.all()로 명령할 수 있다 _set기능을 realted_name을 사용하여 별칭해준다.
      #on_delete=models.CASCADE : user가 삭되되면 user의 모든 정보를 삭제하는 기능

      # host가 Foreignkey로 user를 가리키고 있기 때문에 user는 room_set 엘리먼트를 가지며
      # 마찬가지로 Review의 user변수가 ForeignKey로 User를 가리키고 있기 때문에
      # user는 또한 review_set 엘리먼트(매서드)를 가지고 있다

      room_type = models.ForeignKey("RoomType", related_name = "rooms", on_delete=models.SET_NULL, null=True)
      amenities = models.ManyToManyField("Amenity", related_name = "rooms", blank=True)
      facilities = models.ManyToManyField("Facility", related_name = "rooms", blank=True)
      house_rules = models.ManyToManyField("HouseRule", related_name = "rooms", blank=True)
      
      #ManyToMany키는 다음과 같이 사용가능 하다. 
      # room = Room.objects.get(id=1) #id가 1인 방을 객체로 만들어준다.
      # room.amenties.all()

      def __str__(self):
            return self.name
      
      def save(self, *args, **kwargs):
            self.city = str.capitalize(self.city) #city의 첫글자를 대문자로 바꾸어준다
            # self.city = "potato" #city에 어떤것을 입력한던간테 potato가 보여진다.
            super().save(*args, **kwargs) #부모클래스의 save()함수를 override함
            #여기서는 부모의 부보클래스에 save()함수가 있음.
            #부모클래스의 save()는 저장할때만다 바뀐 함수(여기서는 city명의 앞글자를 대문자로)
            #를 적용하여 저장하라는 매서드임.
      #https://docs.djangoproject.com/en/3.0/topics/db/models/
      #위 함수는 super()매서드로 상위클래스나 현재의 클래스를 상속받는 매서드임.
      #결국 현재의 save함수로 city를 지정된 값으로 보여지게 한다. 
      #저장버튼을 눌렀을때 적용되는 함수다.

      # def total_rating(self):
      #       all_reviews = self.reviews.all() #여기서 reviews는 related_set의 reviews이다.
      #       for review in all_reviews:
      #           print(review.rating_average())
      #       return 0

      def total_rating(self): 
            all_reviews = self.reviews.all()
            all_ratings = 0

            if len(all_reviews) > 0:
                  for review in all_reviews:
                        all_ratings += review.rating_average()
                  return round(all_ratings / len(all_reviews), 2)
            return 0

            
            # for review in all_reviews:
            #     all_ratings += review.rating_average()
            
            # if len(all_reviews)  == 0:
            #       return 0
            # else: 
            #       return all_ratings / len(all_reviews)
                


