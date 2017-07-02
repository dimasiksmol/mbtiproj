from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login
from src.apps.personalp.models import Personal_info
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from src.apps.authentification.forms import AuthentificationForm
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.core.exceptions import ValidationError
from django.contrib import messages


#нужна вьюха для формы
def login_for_user(request):
    if request.method == "POST":
        form = AuthentificationForm(request.POST)
        if form.is_valid():
            auth_first_field = request.POST['username']
            auth_second_field = request.POST['password']
            user = authenticate(username=auth_first_field, password=auth_second_field)
            print("request is post")
            if user is not None:
                if user.is_active:
                    login(request, user)
                    pers = Personal_info.objects.get(user=user) #user = username #was an error literal for int()
                    return HttpResponseRedirect(reverse('personalp:personal_info', args=(pers.pk,)))
                else:
                    form = AuthentificationForm(request.POST)
                    messages.error(request, 'Your account is disabled')
                    return render(request, 'auth/auth.html', {'form': form })
                #return HttpResponse("Your account is disabled.")
            else:
                print("User is none")
                form = AuthentificationForm(request.POST)
                messages.error(request, 'Invalid login details supplied.')
                return render(request, 'auth/auth.html', {'form': form })
                # return HttpResponse("Invalid login details supplied.")
        else:
            print("Form is not valid")
            messages.error(request, 'login or password are not correct.')
            return render(request, 'auth/auth.html', {'form':form} )
    else:
        print("No data post")
        return render(request, 'auth/auth.html', {'form' : AuthentificationForm() })


def logout_for_user(request):
    user = None
    logout(request)
    return HttpResponseRedirect(reverse('registration:index'))



#try:
                    #    current_user = Personal_info.objects.get(username=auth_first_field)
                    ##except:
                     #   current_user = Personal_info.objects.get(email=auth_first_field)
                    #finally:
                        #print("Net takogo username or email")
                        #form = AuthentificationForm(request.POST)
                        #return render(request, 'auth/auth.html', {'form': form})
                    #current_user.ip_address = request.META['REMOTE_ADDR']
                    #current_user.last_activity = datetime.now()
                    #current_user.save()





