from django.conf.urls import url

from . import views

urlpatterns = [



    url(r'^$', views.about, name = "about" ), #VIKTIGT ATT DENNA ÄR SIST

    #url(r'^recipe_match', views.recipes, name="recipe_match"),


    ]