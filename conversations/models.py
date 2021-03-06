from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampModel):

        participants = models.ManyToManyField("users.User", related_name = "conversation", blank=True)
        # def __str__(self):
        #         return str(self.created)

                #return self.created
                #이런 경위 created가CharField가 아니므로 에러가 나므로 created를 반환하여
                #표기에 나타나도록 하고 싶으면 str로 감싸준다.
        
        #위처럼 하면 날짜와 시간이 보기 흉하게 보여지므로 아래와 같이 수정한다. 
        def __str__(self):
                usernames = []
                for user in self.participants.all():
                        usernames.append(user.username)
                return ", ".join(usernames)

        def count_messages(self):
                return self.messages.count()
        count_messages.short_description = "Number of Messages"

        def count_participants(self):
                return self.participants.count()

        count_participants.short_description = "Number of participants"
        
        

        

class Message(core_models.TimeStampModel):

        message = models.TextField()
        user = models.ForeignKey("users.User", related_name = "messages", on_delete = models.CASCADE)
        conversation = models.ForeignKey("Conversation",  related_name = "messages", on_delete=models.CASCADE)

        def __str__(self):
                return f"{self.user} says: {self.message}"