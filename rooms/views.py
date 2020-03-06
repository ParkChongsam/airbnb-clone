# from math import ceil
# from datetime import datetime

# from django.core.paginator import Paginator, EmptyPage
# from django.utils import timezone

from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
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

def room_detail(request, pk): #여기서 pk를 potato라고 써도 된다.
    #물론 rooms.urls.py 에서 <int:potato>라고 똑같이 써주면 된다. 
    # print(pk)
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room":room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home")) #예외발생하는 경우 core:home 으로 가기
        raise Http404()  #404페이지를 띄워라 
        #내가 원하는 문구가 나오에 하려면 templates 바로 밑에 404.html만 만들어 주면 된다.
        #이경우 settings.py를 아래와같이 바꾸어주어야함.
        # DEBUG = False
        # ALLOWED_HOSTS = "*"




        #아래처럼 Class View에 함수(funtion based view)를 추가 할 수도 있다.

        # def get_context_data(self, **kwargs):
        #         context = super().get_context_data(**kwargs) #room의 모든 리스트를 가져온다. 
        #         now = timezone.now()
        #         context["now"] = now
        #         return context



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



