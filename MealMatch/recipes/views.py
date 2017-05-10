
from .models import *
from  account_functions.models import Profile

from django.http import JsonResponse
from bson.json_util import dumps
import re

from collections import OrderedDict
from bson.objectid import ObjectId
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from account_functions.context_processors import get_user
from account_functions.views import *

from .forms import CommentForm

from account_functions.decorators import check_recaptcha


############# VIEW FUNCTIONS #####################
def startpage(request):
    if (request.method == "GET"):
        return render(request, "startpage.html")



##Queries and renders a recipe when a recipe in the result list is clicked##
@check_recaptcha
def presentRecipe(request):
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid() and request.recaptcha_is_valid:

            recipe_id = request.path[-24:]
            try:
                mongouser = Profile.objects.get(user_id_reference=request.user.id)
                recipe_response = recipe.objects.get(_id=ObjectId(recipe_id))
            except:
                pass  # display modal saying "could not comment"
            else:

                comment = Comment(author=mongouser.id, body=form.cleaned_data.get("comment"),
                                  username=request.user.username)
                recipe_response.update(add_to_set__comment=comment)
                recipe_response.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    elif not request.recaptcha_is_valid:


        pass



    if request.method == "GET": #When the page is retrieved
        req_id = request.path[-24:] #Extracts the id from the path
        recipe_response = recipe.objects.get(_id = ObjectId(req_id))#Runs query with the request ID



        try:
            recipe_rating = get_ratings(req_id)
        except:
            recipe_rating = 1
            print('bajsrating')

        try:
            comments_query = recipe_response.comment #check if recipe has comments
        except:
            comments = None
        else:
            comments = getComments(comments_query)

        print('vad skickar u? ', recipe_rating)
        return render(request, "presenterarecept.html", {"recipe": recipe_response, "comments": comments or None, "commentform": CommentForm, "rating" : recipe_rating})








##Queries user inputs on database and renders a result list##
def retrieveRecipes(request):

    if request.method == "GET":
        raw_input = request.path[17:-1].split("&") #splits into array based on &, title() makes first letters capitalized (to be reomved?)
        input = []
        for element in raw_input:
            input.append(sanitize(element)) #Sanitizses !! IMPORTANT !!
        # Now that the input is cleaned, we can implement elasticsearch/fuzzy search on food_ref t

        query_mapped = mapped.objects(id__in=input).only('value').key_frequency()#queries from the mapped colletion and does a key_frequency check
        sorted_dict = OrderedDict(reversed(sorted(query_mapped.items(), key=lambda x: (x[1]['frequency']/x[1]['ing_count']*x[1]['frequency'], x[1]['clicks'], x[1]['rating'])))) #Sorts list based on frequency
        dictlist = []
        for key, value in sorted_dict.items():
            temp = [key,value]
            dictlist.append(temp)
        paginator = Paginator(dictlist, 12)  # Show 9 contacts per page
        page = request.GET.get('page', 1)




        recipes = view_paginator(page, paginator)
        page_range = paginateSlice(3, recipes, paginator)

        return render(request, "recipes.html", {"user_input" : input, "recipes": recipes, "page_range" : page_range, "num_pages": paginator.num_pages})
    else:
        return render(request, "startpage.html")

##Autocorrect implementation. Must be adjusted to prevent crashed (eg via elasticsearch or fewer queries)##
def autocorrect(request):
    input = sanitize(request.POST['input'])  # gets the user input and sanitizses using sanitize()
    if (len(input) > 0):

        array = []
        foods = food_ref.objects(food__istartswith=input)  # checks if any word starts with the user input
        for element in foods:
            array.append(element.food)  # appends matches to an initially empty array
        array = dumps(array)  # dumps the aray to JSON format
        return JsonResponse(array, safe=False)  # returns a JSONResponse to client-side
    else:
        return render(request, "startpage.html") #if there is no input, do as before






############# HELPER FUNCTIONS #############
def sanitize(user_string):
    user_string = re.sub("_", " ", user_string)  # Converts underscore to whitespace
    user_string = re.sub("[^a-öA-Ö],[^-]","", user_string) #removes non alphabetic characters but allows whitespcae and single dash
    user_string = re.sub("--", "", user_string)#removes double dash to prevent injections
    return user_string


def getComments(comments_query):
    comments = []
    for comment in comments_query:
        try:
            user = Profile.objects.get(_id=comment.author) #ensure user exists
        except:
            pass #else, throw comment away
        else:
            comment = comment.to_mongo().to_dict()
            comment['picture'] = user.picture
            comments.append(comment)
    return comments

def view_paginator(page, paginator):
    try:
        recipes = paginator.page(page)
        return recipes
    except PageNotAnInteger:
        recipes = paginator.page(1)
        return recipes
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)
        return recipes


def paginateSlice(page_numbers, recipes, paginator):
    index = recipes.number - 1 # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - page_numbers + 1 if index >= page_numbers else 0
    end_index = index + page_numbers if index <= max_index - page_numbers else max_index
    # My new page range
    page_range = paginator.page_range[start_index:end_index]

    return page_range

def get_ratings(id):

    ratings = recipe.objects.get(_id = ObjectId(id)).ratings


    print ('vad är ratings? ' , ratings )
    sum = 0
    for item in ratings:
        print('vad är detta? ',item)
        sum =+ item
    rating = sum/len(ratings)
    print('rating ', rating)


    return rating

def starrating(request):

    recipe_use = recipe.objects.get(_id=ObjectId(request.POST['recipe_id']))
    print('recipe_use', recipe_use)
    recipe_use.rating.append(request.POST['rating'])
    print('bajs', request.POST['rating'] )
    recipe.save()