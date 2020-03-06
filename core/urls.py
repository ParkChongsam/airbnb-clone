from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [path("", room_views.HomeView.as_view(), name = "home")]
#함수가 와야 하는데 HomeView는 클래스이다 이것을 함수로 인식하게 해주는 as_view()매서드 사용.