from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampModel):

        participants = models.ManyToManyField("users.User", blank=True)
        def __str__(self):
                return str(self.created)

                #return self.created
                #이런 경위 created가CharField가 아니므로 에러가 나므로 created를 반환하여
                #표기에 나타나도록 하고 싶으면 str로 감싸준다.

class Message(core_models.TimeStampModel):

        message = models.TextField()
        user = models.ForeignKey("users.User", on_delete=models.CASCADE)
        conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

        def __str__(self):
                return f"{self.user} says: {self.text}"

