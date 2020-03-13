from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")  # reverse는 core:home로 가서 실제 url을 주는 매서드

    # 기존 이메일과 패스워드가 있는지 확인하기(validating)
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignupView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("core:home")  # reverse는 core:home로 가서 실제 url을 주는 매서드
    initial = {
        "first_name": "park",
        "last_name": "sam",
        "email": "inkservice2@naver.com",
    }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get("email")
            # email이 있는지 확인해서 있다면 아래코드(raise)를 실행하기
            raise froms.ValidationError("User already exists")
        except models.User.DoesNotExist:
            # models.User.DoesNotExist 이 에러 발생시 email을 입력한 이메일을 반환한다(사용한다)
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

