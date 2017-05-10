from django import forms
from .models import *
from mongoengine.django.auth import *
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        #user = authenticate(username = username, password = password)
        if username and password:
            user=authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
        return super(UserLoginForm, self).clean()




class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget = forms.PasswordInput, required = True)
    mail = forms.CharField(required=True)


    def check_username(self):
        username = self.cleaned_data.get('username')
        try:
            q1 = User.objects.get(username=username)
            raise forms.ValidationError("This username is already taken")
        except DoesNotExist: #if no users in the database exist with that particular username

            return username


#class Addingridient(forms.ModelForm):
#    ingridient = forms.CharField()

class AddRecipeForm(forms.Form):
    title = forms.CharField(label ='Title')
    directions = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Please enter the description of how to make your recipe'}), label = 'Description')
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter the ingridients for the recipe with the corresponding amount, seperate each ingridient with a " : "'}), label = 'Ingridients and amount', help_text = '2 gallons of milk : 1kg of flour : 1 tablespoon of salt, for example.' )
    category = forms.CharField(required=False,label = 'Category',widget=forms.TextInput(attrs={'placeholder': 'Please enter the category/categorys that your recipe belongs to, seperate each category with a " : " '}), help_text = 'Mexican : Bread : Medeteranian, for example')
    picture_url = forms.URLField(required=False, label = 'Picture',widget=forms.TextInput(attrs={'placeholder': 'Please enter the url for the picture dsiplaying your recipe'}))
    preperation_time = forms.CharField(required=False, label = 'Preperation time',widget=forms.TextInput(attrs={'placeholder': 'Please enter the preparation time with given unit'}), help_text = '1h and 20min, for example')
    servings = forms.IntegerField(required=False, label = 'Servings with the given amount of ingredients')






# class UserRegisterForm(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(widget = forms.PasswordInput, required = True)
#     mail = forms.CharField(required=True)
#
#
#     def check_username(self):
#         username = self.cleaned_data.get('username')
#         try:
#             q1 = User.objects.get(username=username)
#             raise forms.ValidationError("This username is already taken")
#         except DoesNotExist: #if no users in the database exist with that particular username
#             print("test")
#             return username




class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='Confirm email')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
            'email',
            'email2'
        ]
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        return password

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email


