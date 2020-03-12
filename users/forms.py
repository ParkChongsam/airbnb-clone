from django import forms

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    #widget=forms.PasswordInput - 패스워드가 * 표시로만 보이는 파라미터





#장고는 username을 중요하게 생각함.생각함
#username을 email인 것처럼 사용해서 appplication을 만든다. - user중복 체크하기 위함.