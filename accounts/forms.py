# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.models import User
# from django.db import transaction
# from .models import User

# class SignUpForm(UserCreationForm):
#     # first_name = forms.CharField(label='First Name', required=False)
#     # last_name = forms.CharField(label='Last Name', required=False)
#     # # verify_code = forms.IntegerField(required=False)
#     # email = forms.EmailField(max_length=254, help_text='Required a valid email address.', required=False)
#     # phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
#     # phone_number = forms.IntegerField(null=False, required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = [
#                     'username',
#                     'phone',
#                     # 'verify_code',
#                     'password1',
#                     'password2',
#                 ]

#     @transaction.atomic
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_executive = False
#         user.save()
#         # normal_user = NormalUser.objects.create(user=user)
#         # normal_user.first_name = self.cleaned_data['first_name']
#         # normal_user.last_name = self.cleaned_data['last_name']
#         return user
