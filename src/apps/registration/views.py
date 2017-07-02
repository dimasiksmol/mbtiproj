from django.shortcuts import get_object_or_404, render
from src.apps.registration.forms import UserForm
from src.apps.registration.forms import Personal_info_form
from src.apps.personalp.models import Personal_info
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        user = request.user
        print('---------------------------------------------')
        print(user)
        print('---------------------------------------------')
        pers = Personal_info.objects.get(user=user)
        print('---------------------------------------------')
        print(pers)
        print('---------------------------------------------')
        return render(request, 'main.html', {'pers': pers})
    else:
        return render(request, 'main.html')

def register(request):
    if request.method == 'POST':
        #данные, полученные из 2 форм для пользователя и персональной информации
        user_form = UserForm(request.POST)
        profile_form = Personal_info_form(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            print('form is valid')
            print('-------------')
            print(user_form['username'])
            print('-------------')
            print(profile_form)
            print('-------------')
            print(user_form)
            profile = profile_form.save()
            #try save profile first to avoid errors #the password not in latin letters was raise an error
            user = user_form.save()
            user.save()
            profile.user = user
            profile.save()
            user = authenticate(username=user_form['username'], password=user_form['password1'])
            print('-----user-----')
            print(user)
            print('-----user-----')
            login(request, user)
            #pers = Personal_info.objects.get(user=user)
            return HttpResponseRedirect(reverse('personalp:personal_info', args=(profile.pk,)))
        else:
            print('form is not valid')
            user_form = UserForm(request.POST)
            profile_form = Personal_info_form(request.POST, request.FILES)
            errors_form1 = user_form.errors
            errors_form2 = profile_form.errors
            print(errors_form1)
            print(errors_form2)
            return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form,
                                                                  'errors_form1':errors_form1, 'errors_form2':errors_form2})
    else:
        print('form is not send')
        user_form = UserForm()
        profile_form = Personal_info_form()
        return render(request, 'registration/register.html', { 'user_form': user_form, 'profile_form': profile_form })


        # new_registered = Personal_info.objects.create()
        ##new_registered.nick_name = profile_form.cleaned_data["nick_name"]
        # new_registered.birth_date = profile_form.cleaned_data["birth_date"]
        ##new_registered.location = profile_form.cleaned_data["location"]
        # new_registered.img_pers = profile_form.cleaned_data["img_pers"]
        # new_registered.gender = profile_form.cleaned_data["gender"]
        # new_registered.save()

        # user_data = user_form.cleaned_data
        # user.username = user_data['username']
        # user.first_name = user_data['firstname']
        # user.last_name = user_data['lastname']
        # user.email = user_data['email']
        # user.set_password(user_data['pass1'])

        # пустая профиль пользователя
        # empty_Personal_info = Personal_info()
        # empty_Personal_info_data = profile_form.cleaned_data
        # empty_Personal_info.nick_name = empty_Personal_info_data['nick_name']
        # empty_Personal_info.gender = empty_Personal_info_data['gender']
        ##empty_Personal_info.location = empty_Personal_info_data['location']
        ##empty_Personal_info.img_pers = empty_Personal_info_data['img_pers']
        # empty_Personal_info.birth_date = empty_Personal_info_data['birth_date']
        # empty_Personal_info.save()

            #user_username = form.cleaned_data["username"]
            #user_password = form.cleaned_data["password1"]
            #user_email = form.cleaned_data["email"]
            #user_first_name = form.cleaned_data["first_name"]
            #user_last_name = form.cleaned_data["last_name"]
            #new_registered = Personal_info.objects.create_user(user_username,user_password,user_email)
            #new_registered.first_name = form.cleaned_data["first_name"]
            #new_registered.last_name = form.cleaned_data["last_name"]
            #new_registered.nick_name = form.cleaned_data["nick_name"]
            #new_registered.img_pers = form.cleaned_data["img_pers"]
            #new_registered.nick_name = form.cleaned_data["nick_name"]
            #new_registered.nick_name = form.cleaned_data["nick_name"]
            #new_registered_user.save()
            #return HttpResponseRedirect(reverse('personalp:personal_info', args=(new_registered.pk,)))