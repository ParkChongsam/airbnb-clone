from django.db import models
from core import models as core_models

class Review(core_models.TimeStampModel):


      """ Review Model Definition """

      review = models.TextField()
      accuracy = models.IntegerField()
      communication = models.IntegerField()
      cleanliness = models.IntegerField()
      location = models.IntegerField()
      location = models.IntegerField()
      check_in = models.IntegerField()
      value = models.IntegerField()
      user = models.ForeignKey("users.User", related_name = "reviews", on_delete=models.CASCADE)
      #user는 users 앱의 User를 가리켜야 한다. 
      room = models.ForeignKey("rooms.Room", related_name = "reviews", on_delete=models.CASCADE)
      #views의 room은 rooms앱의 Room을 가리키는 것이다. 

      def __str__(self):
                  #   return self.room.host.username
                     #현재의 모델의 room에서 rooms.Room으로 가서 다시
                     #Room의 host에서 users앱 model의 username(장고에서 자동생성됨)을 호출하여 
                     #관리자 페이지에 표시해주는 방법임.



                    return f"{self.review} - {self.room}"
                    #위처럼 formating 방법을 사용해서 표시할 수도 있다.
                    #위처럼 return을 적용하면 park.review_set.all()의 값은
                    #return의 값으로 출력된다. 

      def rating_average(self):
            avg =(
                self.accuracy
                + self.communication
                + self.cleanliness
                + self.location
                + self.check_in
                + self.value
            )/6
            return round(avg, 2)   

      rating_average.short_description = "AVG." #단축표현으로 출력되게 함. 




                     
                  
                  
      
