from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

def include_login_form(request):
    form = UserLoginForm(request.POST or None)
    return {'loginForm': form}


def get_user(request):
    try:
        mongouser = Profile.objects.get(user_id_reference = request.user.id)
    except:
        mongouser = None
    return{'user': request.user, 'mongouser': mongouser}


