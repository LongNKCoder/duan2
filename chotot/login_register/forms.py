from django import forms
from django.core import validators
from django.contrib.auth.models import User
from login_register.models import Profile

def check_phone(value):
    if value[0:3].lower() not in ('086','096','097','098','089','090','093','088','091','094','099','092','056','058') or value[0:4].lower() not in ('0162','0163','0164','0165','0166','0167','0168','0169','0120','0121','0122','0126','0128','0123','0124','0125','0127','0129','0199'):
        raise forms.ValidationError("Số điện thọai bạn nhập không có thật")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class ProfileForm(forms.ModelForm):
    # name = forms.CharField()
    # email = forms.EmailField()
    # verify_email = forms.EmailField(label='Nhập email bạn lần nữa')
    # phone = forms.CharField(max_length=11, validators=[check_phone], required=True)
    # password = forms.PasswordInput()
    # verify_pass = forms.PasswordInput()
    class Meta:
        model = Profile
        fields = ('phone','pic')
    # def clean(self):
    #     all_clean_data = super().clean()
        # email = all_clean_data['email']
        # verify_email = all_clean_data['verify_email']
        # password = all_clean_data['password']
        # verify_pass = all_clean_data['verify_pass']

        # if email != verify_email :
        #     raise forms.ValidationError("Email bạn nhập chưa đúng")

        # if password != verify_pass :
        #     raise forms.ValidationError("Email bạn nhập chưa đúng")