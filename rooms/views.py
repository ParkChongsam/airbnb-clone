# from math import ceil
# from datetime import datetime

# from django.core.paginator import Paginator, EmptyPage
# from django.utils import timezone
# from django.http import Http404


from django.shortcuts import render
from django_countries import countries
from django.views.generic import ListView, DetailView
from . import models

#https://docs.djangoproject.com/en/3.0/topics/db/queries/

#class View https://docs.djangoproject.com/en/3.0/ref/class-based-views/

class HomeView(ListView):
    """HomeView Definition"""
    model = models.Room
    #ListView이 속성을 아래사이트에서 다 볼 수 있다.  
    # http://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created" 
    #room models의 Room클래스는 TimeStampModel 을 상속함. class Room(core_models.TimeStampModel)
    #그래서 created을 사용할 수 있음.
    context_object_name = "rooms"


class RoomDetail(DetailView):
    """RoomDetail Definition"""
    model = models.Room

"""RoomDetail Definition based on function"""

# def room_detail(request, pk): #여기서 pk를 potato라고 써도 된다.
#     #물론 rooms.urls.py 에서 <int:potato>라고 똑같이 써주면 된다. 
#     # print(pk)
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room":room})
#     except models.Room.DoesNotExist:
#         # return redirect(reverse("core:home")) #예외발생하는 경우 core:home 으로 가기
#         raise Http404()  #404페이지를 띄워라 
        #내가 원하는 문구가 나오에 하려면 templates 바로 밑에 404.html만 만들어 주면 된다.
        #이경우 settings.py를 아래와같이 바꾸어주어야함.
        # DEBUG = False
        # ALLOWED_HOSTS = "*"
"""Search Definition based on function"""
def search(request):
    city = request.GET.get("city", "Anywhere") #디폴트는 Anywhere로 하기
    city = str.capitalize(city)
    country = request.GET.get("country", "KR") #디폴트는 KR로 하기
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    room_type = int(request.GET.get("room_type", 0)) #디폴트는 어떤 방이든 나오게 0으로 처리하기
    instant = request.GET.get("instant", False)
    super_host = request.GET.get("super_host", False) #()안의 super_host는 search 에서 임의로 지정한 name = "super_host"의 이름을 넣어준다.
    s_amenities = request.GET.getlist("amenities") #amenity를 선택한 항목리스트
    s_facilities = request.GET.getlist("facilities") #facility를 선택한 항목리스트
    s_house_rules = request.GET.getlist("house_rules")
    form = {"city":city,
            "s_room_type": room_type,
            "s_country":country,
            "price":price, 
            "guests":guests, 
            "beds":beds, 
            "baths":baths,
            "s_amenities":s_amenities,
            "s_facilities":s_facilities,
            "s_house_rules":s_house_rules,
            "instant":instant,
            "super_host":super_host,
    }
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    house_rules = models.HouseRule.objects.all()
    choices ={
        "countries":countries,
        "room_types":room_types,
        "amenities":amenities,
        "facilities":facilities,
        "house_rules":house_rules,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city
    # print(filter_args)

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] =room_type

    if price != 0:
        filter_args["price__lte"] = price
    
    if guests != 0:
        filter_args["guest__gte"] = guests

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["Baths__gte"] = baths
    # print(bool(instant), bool(super_host))

    if instant is True:
        filter_args["instant_book"] = True

    if super_host is True:
        filter_args["host__superhost"] = True #rooms models에 super_host 불리언이 없으니
        #ForeignKey키로 rooms의 host에서 user의 superhost로 연결해준다.


    rooms = models.Room.objects.filter(**filter_args)

    return render(request, "rooms/search.html",{**form, **choices, "rooms":rooms})



        #아래처럼 Class View에 함수(funtion based view)를 추가 할 수도 있다.

        # def get_context_data(self, **kwargs):
        #         context = super().get_context_data(**kwargs) #room의 모든 리스트를 가져온다. 
        #         now = timezone.now()
        #         context["now"] = now
        #         return context

"""HomeView Definition based on function"""

#아래 함수 이름 all_rooms이름은 core.urls.py 파일내의 
#urlpatterns = [path("", room_views.all_rooms, name = "home")] 여기의
#.all_rooms과 같아야 함.

# def all_rooms(request):
#         page = request.GET.get("page", 1)
#         room_list = models.Room.objects.all()
#         paginator = Paginator(room_list, 10, orphans=2) #한페이지에 10개씩 보이기
#         #orphans = 5, 마지막 페이지에 있는 리스트가 5이하이면 그전페이지에 같이 보여줌
#         #5 이상이면 마지막페이지에 보여줌
#         try:
#                 rooms = paginator.page(int(page))
#                 return render(request, "rooms/home.html", {"page":rooms})
#         except EmptyPage:
#                 return redirect("/") #home으로 리다리렉트하라는 명령


        
        #django에게 home.html를 컴파일하라고 명령하기

        #여기서 home.html의 home이름은 all_rooms = models.Room.objects.all() 여기의
        #all_rooms 이름과 같지 않아도 된다. 예)home.html이라고 해도 된다ㅏ. 
        #그러나 이 home.html이라고 했으면 이 이름은 templates에있는 html이름과 동일하여야함.



