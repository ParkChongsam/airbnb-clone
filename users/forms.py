from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # widget=forms.PasswordInput - 패스워드가 * 표시로만 보이는 파라미터

    def clean(self):  # 여기서 매서드 이름은 clean을 반드시 해준다.
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                # chck_password 패스워드 암호화
                # https://docs.djangoproject.com/en/3.0/ref/contrib/auth/

                # return password
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is worng"))

        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))

            # raise forms.ValidationError("User does not exist")


class SignupForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")


# 장고는 username을 중요하게 생각함.생각함
# username을 email인 것처럼 사용해서 appplication을 만든다. - user중복 체크하기 위함.

