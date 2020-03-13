# from django.views import View
# from django.views.generic import FormView
# from django.urls import reverse_lazy
# from django.shortcuts import render, redirect, reverse
# from django.contrib.auth import authenticate, login, logout
# from . import forms


# class LoginView(FormView):

#     template_name = "users/login.html"
#     form_class = forms.LoginForm
#     success_url = reverse_lazy("core:home")  # reverse는 core:home로 가서 실제 url을 주는 매서드

#     # 기존 이메일과 패스워드가 있는지 확인하기(validating)
#     def form_valid(self, form):
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         user = authenticate(self.request, username=email, password=password)
#         if user is not None:
#             login(self.request, user)
#         return super().form_valid(form)


# def log_out(request):
#     logout(request)
#     return redirect(reverse("core:home"))


# class SignUpView(FormView):

#     template_name = "users/signup.html"
#     form_class = forms.SignupForm
#     success_url = reverse_lazy("core:home")  # reverse는 core:home로 가서 실제 url을 주는 매서드
#     initial = {
#         "first_name": "park",
#         "last_name": "sam",
#         "email": "inkservice2@naver.com",
#     }

#     def form_valid(self, form):
#         form.save()  # form이 유효한 경우에 form을 저장하기
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         user = authenticate(self.request, username=email, password=password)
#         if user is not None:
#             login(self.request, user)
#         return super().form_valid(form)


# from django import forms
# from . import models


# class LoginForm(forms.Form):

#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         email = self.cleaned_data.get("email")
#         password = self.cleaned_data.get("password")
#         try:
#             user = models.User.objects.get(email=email)
#             if user.check_password(password):
#                 return self.cleaned_data
#             else:
#                 self.add_error("password", forms.ValidationError("Password is wrong"))
#         except models.User.DoesNotExist:
#             self.add_error("email", forms.ValidationError("User does not exist"))


# class SignUpForm(forms.Form):

#     first_name = forms.CharField(max_length=80)
#     last_name = forms.CharField(max_length=80)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         try:
#             models.User.objects.get(email=email)
#             raise forms.ValidationError("User already exists with that email")
#         except models.User.DoesNotExist:
#             return email

#     def clean_password1(self):
#         password = self.cleaned_data.get("password")
#         password1 = self.cleaned_data.get("password1")
#         if password != password1:
#             raise forms.ValidationError("Password confirmation does not match")
#         else:
#             return password

# def save(self):
#     first_name = self.cleaned_data.get("first_name")
#     last_name = self.cleaned_data.get("last_name")
#     email = self.cleaned_data.get("email")
#     password = self.cleaned_data.get("password")
#     user = models.User.objects.create_user(email, email, password)
#     user.first_name = first_name
#     user.last_name = last_name
#     user.save()

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

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


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {"first_name": "Nicoas", "last_name": "Serr", "email": "itn@las.com"}

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
