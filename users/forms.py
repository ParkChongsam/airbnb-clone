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
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.Form):

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    # 장고는 username을 중요하게 생각함.생각함
    # username을 email인 것처럼 사용해서 appplication을 만든다. - user중복 체크하기 위함.

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            # email이 있는지 확인해서 있다면 아래코드(raise)를 실행하기
            raise forms.ValidationError("User already exists with that email")
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

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = models.User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
