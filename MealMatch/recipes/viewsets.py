from rest_framework_mongoengine import viewsets
from recipes.serializers import *

### viewset for API



class recipeViewSet(viewsets.ModelViewSet):

    lookup_field = 'id'#Oklart
    serializer_class = recipeSerializer



    def get_queryset(self):
        return recipe.objects()

class mappedViewSet(viewsets.ModelViewSet):
    #lookup_field = 'id'  # Oklart
    serializer_class = mappedSerializer


    def get_queryset(self):
        return mapped.objects().exclude('id')

