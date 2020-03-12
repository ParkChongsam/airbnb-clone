from django.views import View
from django.shortcuts import render
from . import forms

class LoginView(View):

    def get(self, request):

        form =forms.LoginForm(initial={"email": "inkservice@naver.com"})

        return render(request, "users/login.html", {"form":form})

    def post(self, request):

        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  #cleaned_data는 모든필드를 정리해준거에 대한 결과다.
        return render(request, "users/login.html", {"form":form})
