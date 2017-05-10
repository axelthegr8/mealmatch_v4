def recipes(request):
    #print(request.COOKIES.get('input').split(',')) #Splits the cookies up (which comes as a string) into an array
    #-- remember to sanitize the list before request is sent to sever
    input = request.COOKIES.get('input').split(',')

    arr = []
    recipe_array = []
    for item in input:
        arr.append(queryMapped(item))


    #Intersect-funktioner etc


    for object in arr:
        temp_array = list(object.value.keys())

        for index in range(len(temp_array)):
            temp_array[index] = stripAndObjectify(temp_array[index])

        recipe_array.append(temp_array)
        temp_array = []









    test_recipe = []
    for index in range(len(recipe_array[0])):
        test_recipe.append((recipe.objects.get(id = recipe_array[0][index])))





    #print(type(result))



########################
    #recipe_query = recipe.objects.get(id =result)
    #print(recipe_query.title)


##################
    #for rec in recipe.objects:
        #print(type(rec.id))

    #recipe_query = recipe.objects.get(title__icontains = result)
    #print(recipe_query)

    #for item in foods_query:
     #   print(item.value)


    return render(request, "recipes.html", {"recipe_array":test_recipe})

def stripAndObjectify(result): #Strips the data from bad formatting (mongoengine bug?) and sets it to an object id

    result = result[8:]
    result = result.strip('("")')

    result = bson.objectid.ObjectId(result)

    return result


def queryMapped(item): #Returns a query from the mapped collection. Matches icontaint on the id field of mapped collection
    return mapped.objects.get(id__icontains=item)