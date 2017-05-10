from mongoengine import *
import mongoengine
import datetime
from django.db import models
from django.contrib import admin
import datetime
from recipes.models import recipe

# Create your models here.
#class comments(Document):
 #   recipe_id = StringField(required=True)
  #  user_comment = StringField(required=True)


from django.db import models
from django.contrib.auth.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

#
# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     pass
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_filter = ['is_staff']
#     pass



class user_test(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)



class Profile(DynamicDocument):
    user_id_reference = IntField(unique=True)
    full_name = StringField()
    first_name = StringField()
    last_name = StringField()
    date = DateTimeField(default=datetime.datetime.now())
    facebook_id = IntField()
    favorites = ListField()
    my_recipies = ListField()
    #comments = ListField(EmbeddedDocumentField('comments'))
    picture = URLField() #facebook link
    my_info = StringField()
    age = IntField()
    sex = StringField()
    Pantry = ListField(default= ['Salt', 'Sea salt', 'Pepper','White pepper', 'Vinegar', 'Flour', 'Oil', 'Sugar', 'Pasta', 'Baking powder', 'Soy sauce', 'Broth', 'Honey', 'Tomato purée', 'Cinnamon', 'Oregano', 'Curry'])



