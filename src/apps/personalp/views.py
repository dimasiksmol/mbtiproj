from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from src.apps.personalp.forms import PersonalPImg
from . models import Personal_info
from django.contrib.auth.decorators import login_required


app_name = 'personalp'

def index(request):
    return render(request, 'main.html')

def personal_info(request, personal_id):
    pers = get_object_or_404(Personal_info, pk=personal_id)
    print('----------------------------------------------')
    print(request.user)
    #print(request.user.get(username = pers.user))
    print('----------------------------------------------')
    if request.method == "POST":
        #Form for uploading avatar photo
        form = PersonalPImg(request.POST, request.FILES)
        if form.is_valid:
            print(form)
            print('---------------------------------')
            print(pers)
            pers.img_pers = form.cleaned_data['img_pers'] #Был косяк, но он прошел
            pers.save()
        return HttpResponseRedirect(reverse('personalp:personal_info', args = (pers.pk,)))
    else:
        form = PersonalPImg()
    return render(request, 'personalp/personal_index.html', {'pers' : pers, 'form' : form} )