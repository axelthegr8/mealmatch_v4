from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^recipes', views.retrieveRecipes, name="recipes"),
    url(r'^autocorrect', views.autocorrect, name="autocorrect"),
    url(r'^presenterarecept/', views.presentRecipe, name="presenterarecept"),
    url(r'^starrating', views.starrating, name="starrating"),

    url(r'^$', views.startpage, name = "startpage" ), #VIKTIGT ATT DENNA ÄR SIST

    #url(r'^recipe_match', views.recipes, name="recipe_match"),


    ]