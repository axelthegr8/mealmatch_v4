### Custom pipelines for the facebook login ###

from .models import *
import facebook
from bson.objectid import ObjectId


def user_profile(backend, details, response, uid, user, *args, **kwargs):
    pass
  # #social_user.extra_data['access_token'],
  # large_picture = 'http://graph.facebook.com/{0}/picture?type=large&access_token={1}'.format(response['id'], response['access_token'])
  # data = 'https://graph.facebook.com/v2.9/{0}/?fields=gender,age_range,location,picture,name&access_token={1}'.format(response['id'], response['access_token'])
  # gender = 'http://graph.facebook.com/{0}/age_range?&access_token={1}'.format(response['id'], response['access_token'])
  # age =
    if not check_existance(user):
        create_user(details, response, uid, user)

    elif check_existance(user):
        update_user(details, response, uid, user)
    pass


def check_existance(user):
    try:
        nosql_user = Profile.objects.get(user_id_reference = user.id)

        return True
    except:
        return False

def update_user(details, response, uid, user):
        try:
            nosql_user = Profile.objects.get(user_id_reference=user.id)
        except:
            return False
        else:
            graph = facebook.GraphAPI(access_token=response['access_token'], version='2.7')
            args = {'fields': 'id,gender,age_range', }
            userprofile = graph.get_object(id=response['id'], **args)
            nosql_user.age = userprofile['age_range']['min']
            nosql_user.sex = userprofile['gender']
            nosql_user.picture = "https://graph.facebook.com/{0}/picture?type=large&access_token={1}".format(response['id'],response['access_token'])
        pass

def create_user( details, response, uid, user):
    graph = facebook.GraphAPI(access_token=response['access_token'], version='2.7')
    args = {'fields': 'id,gender,age_range', }
    userprofile = graph.get_object(id=response['id'], **args)

    age = userprofile['age_range']['min']
    gender = userprofile['gender']
    large_picture = 'https://graph.facebook.com/{0}/picture?type=large&access_token={1}'.format(response['id'],
                                                                                                response[
                                                                                                    'access_token'])

    profile = Profile(user_id_reference=user.id, full_name=details['fullname'], first_name=details['first_name'],
                      last_name=details['last_name'], facebook_id=uid, picture=large_picture, age=age, sex=gender)
    profile.save()
    pass

