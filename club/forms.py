from django import forms
from .models import UserStaffs, UserMembers, UserDetail
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email']
        read_only = ['id']


class LoginStaffForm(forms.ModelForm):
    class Meta:
        model = UserStaffs
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email']
        read_only = ['id']


class LoginMemberForm(forms.ModelForm):
    class Meta:
        model = UserMembers
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email']
        read_only = ['id']


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['dob', 'address', 'phone_num', 'bio', 'profile_pic']
        read_only = ['id']