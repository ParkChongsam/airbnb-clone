#반드시 폴더이름을 management와 commands로 사용하여야 한다.
#comands로 하여 에러가 나서 헤맸었음.
# (airbnb-clone)  (airbnb-clone-JyVlJi3w) C:\project\airbnb-clone>python manage.py loveyou --times
# AttributeError: module 'rooms.management.commands.loveyou' has no attribute 'Command'

import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models

class Command(BaseCommand):

        help = 'This command creates many rooms'

        def add_arguments(self, parser): #부모클래스(BaseCommand)의 함수(add_arguments)를 가져와서 사용함. super()와 같은 기능?
                parser.add_argument("--number", default=2, type=int, help = "How many rooms do you want to create")
        
        

        def handle(self, *args, **options):
                number = options.get("number")
                seeder = Seed.seeder()
                all_users = user_models.User.objects.all() #모든 user를 변수로 만들어서 가져오기
                room_types = room_models.RoomType.objects.all() #모든 room_type을 변수로 만들어서 가져오기
                #지금은 user가 50명이기 때문에 all()을 사용했지만 유저가 몇십만명정도로
                #많은 경우에는 all()을 사용하면 안됨.

                seeder.add_entity(room_models.Room, number, {
                        "name": lambda x: seeder.faker.address(),
                        #가짜로 만들어주는 faker라이브러리
                        # https://faker.readthedocs.io/en/master/providers/faker.providers.address.html
                        "host": lambda x:random.choice(all_users), 
                        "room_type": lambda x:random.choice(room_types),
                        "guests": lambda x:random.randint(1,10),
                        "price": lambda x:random.randint(1,300),
                        "beds": lambda x:random.randint(1,5),
                        "baths": lambda x:random.randint(1,5),
                        },
                        )
                created_photos = seeder.execute()
                # print(created_photos.values()) #dict_values([[7]]) 1 rooms created!
                # print(list(created_photos.values())) #dict_values([[7]]) 1 rooms created!
                # 그렇지만 결과가 2array임
                #그래서 장고에서 지원해주는 flatten매서드를 사용할것임
                created_clean = flatten(list(created_photos.values()))
                amenities = room_models.Amenity.objects.all()
                facilities = room_models.Facility.objects.all()
                rules = room_models.HouseRule.objects.all()

                for pk in created_clean:
                        room = room_models.Room.objects.get(pk=pk)
                        for i in range(3, random.randint(10, 30)):
                                room_models.Photo.objects.create(
                                        caption=seeder.faker.sentence(),
                                        room = room,
                                        file=f"room_photos/{random.randint(1, 31)}.webp",
                                )
                        for a in amenities:
                                magic_number = random.randint(0,15)
                                if magic_number % 2 == 0:
                                        room.amenities.add(a)

                        for f in facilities:
                                magic_number = random.randint(0,15)
                                if magic_number % 2 == 0:
                                        room.facilities.add(f)

                        for r in rules:
                                magic_number = random.randint(0,15)
                                if magic_number % 2 == 0:
                                        room.house_rules.add(r)

                self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
