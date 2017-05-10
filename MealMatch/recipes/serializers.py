from rest_framework_mongoengine import serializers
from .models import *


### "helper" serializers for embedded documents###
class mappedValueSerializer(serializers.DocumentSerializer): #Defined as a documentserializer because of troublesome id fields

    class Meta:
        model = mapped_id
        depth = 2
        fields = "__all__"


###API serializers file. EQuivalent to model
class recipeSerializer(serializers.DocumentSerializer):

    class Meta:
        depth = 2
        model = recipe
        #fields = "__all__"
        exclude = ("rating","comments", "servings")


class mappedSerializer(serializers.DocumentSerializer):
    value = mappedValueSerializer(many=True)

    class Meta:

        model = mapped
        depth = 2
        exclude = ("id",)



