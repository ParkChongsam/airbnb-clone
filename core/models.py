from django.db import models

class TimeStampModel(models.Model):

      """ Time Stamped Mdel """

      created = models.DateTimeField(auto_now_add=True) #모델일 생성된 날짜 구할때
      updated = models.DateTimeField(auto_now=True) #새로운 날짜로 업데이트하는 기능

      class Meta:
            abstract = True
