from django.db import models
from core import models as core_models

class Review(core_models.TimeStampModel):


      """ Review Model Definition """

      review = models.TextField()
      accuracy = models.IntegerField()
      communication = models.IntegerField()
      cleanliness = models.IntegerField()
      location = models.IntegerField()
      check_in = models.IntegerField()
      value = models.IntegerField()
      user = models.ForeignKey("users.User", on_delete=models.CASCADE)
      #user는 users 앱의 User를 가리켜야 한다. 
      room = models.ForeignKey("rooms.Room" , on_delete=models.CASCADE)
      #views의 room은 rooms앱의 Room을 가리키는 것이다. 

      def __str__(self):
                  #   return self.room.host.username
                     #현재의 모델의 room에서 rooms.Room으로 가서 다시
                     #Room의 host에서 users앱 model의 username을 호출하여 
                     #관리자 페이지에 표시해주는 방법임.



                    return f"{self.review} - {self.room}"
                    #위처럼 formating 방법을 사용해서 표시할 수도 있다.
                    




                     
                  
                  
      
