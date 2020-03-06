"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#바로 위는 첨부사진을 클릭했을때 보여지게 하는 방법임.
#위에서 static을 import해주어야함.
#위 if문은 AWS나 다른 서버에서 이 프로젝트를 실행시킬때는 필요없는 코드이며 그때는 
#AWS에 맞는 코드를 작성해주어야함.  - AWS에 업로드할때 Nico가 가르쳐준다고함. 
#지금은 개발단계임(DEBUG = True)


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     # path("", include("core.urls", namespace="core")),
#     # path("rooms/", include("rooms.urls", namespace="rooms")),
#     # path("users/", include("users.urls", namespace="users")),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
