#반드시 폴더이름을 management와 commands로 사용하여야 한다.
#comands로 하여 에러가 나서 헤맸었음.
# (airbnb-clone)  (airbnb-clone-JyVlJi3w) C:\project\airbnb-clone>python manage.py loveyou --times
# AttributeError: module 'rooms.management.commands.loveyou' has no attribute 'Command'

from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User

class Command(BaseCommand):

        help = 'This command creates many users'

        def add_arguments(self, parser): #부모클래스(BaseCommand)의 함수(add_arguments)를 가져와서 사용함. super()와 같은 기능?
                parser.add_argument("--number", default=2, type=int, help = "How many users do you want to create")
        
        def handle(self, *args, **options):
                number = options.get("number")
                seeder = Seed.seeder()
                seeder.add_entity(User, number, {'is_staff':False, "is_superuser":False})
                
                #여기서 {'is_staff':False, "is_superuser":False} 이부분은 옵션으로 원래 Abstractuser
                #클래스에서 디폴트가 staff status와 superuser status가 체크되는게 디폴트인데
                #이 변수를 체크 안하는 디폴트로 바꾸어 줄려고 매개변수를 찾아서 넣어준것이다.)
                #이 매개변수를 찾는 방법은 import된 User의 부모클래스(Abstractuser)에 가서 찾아온것이다. 
                #이런 형태의 코드 작성이 아주 유용하다. 

                seeder.execute()
                self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
 
                # times = options.get("times")
                # for t in range(0, int(times)):
                #         self.stdout.write(self.style.SUCCESS("I love you"))
