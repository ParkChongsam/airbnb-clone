#반드시 폴더이름을 management와 commands로 사용하여야 한다.
#comands로 하여 에러가 나서 헤맸었음.
# (airbnb-clone)  (airbnb-clone-JyVlJi3w) C:\project\airbnb-clone>python manage.py loveyou --times
# AttributeError: module 'rooms.management.commands.loveyou' has no attribute 'Command'

from django.core.management.base import BaseCommand
from rooms.models import Facility

class Command(BaseCommand):

        help = 'This command creates facilities'

        def add_arguments(self, parser): #부모클래스(BaseCommand)의 함수(add_arguments)를 가져와서 사용함. super()와 같은 기능?
                parser.add_argument("--times", help = "How many time do you want me to tell that I love you")
        
        def handle(self, *args, **options):

                facilities = [
                     "Private entrance",
                     "Paid parking on premises",
                     "Paid parking off premises",
                     "Elevator",
                     "Parking",
                     "Gym",
                ]

                for f in facilities:
                        Facility.objects.create(name=f)
                self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
 
                # times = options.get("times")
                # for t in range(0, int(times)):
                #         self.stdout.write(self.style.SUCCESS("I love you"))


# (airbnb-clone)  (airbnb-clone-JyVlJi3w) C:\project\airbnb-clone>python manage.py loveyou --times
# AttributeError: 'Command' object has no attribute 'run_from_argv'
#Basecommand를 import한다.
# (airbnb-clone)  (airbnb-clone-JyVlJi3w) C:\project\airbnb-clone>python manage.py loveyou --times
# hello
# usage: manage.py loveyou [-h] [--version] [-v {0,1,2,3}] [--settings SETTINGS]
#                          [--pythonpath PYTHONPATH] [--traceback] [--no-color]
#                          [--force-color]
# manage.py loveyou: error: unrecognized arguments: --times
# help = 'This command tells me'를 넣어준다
# (airbnb-clone)  (airbnb-clone-JyVlJi3w) C:\project\airbnb-clone>python manage.py loveyou
#NotImplementedError: subclasses of BaseCommand must provide a handle() method

