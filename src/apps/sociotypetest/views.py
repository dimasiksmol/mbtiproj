from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from src.apps.personalp.models import Personal_info
from .models import Socionic_type
from .forms import sociotype_test

# общий юрл sociotypetest

    # view test result
def sociotest(request, personal_id):
    pers = get_object_or_404(User, pk=personal_id)
    if request.method == 'POST':
        #если форма отправлена и валидна, проитерировать поля формы и записать результат в дихотомии
        form = sociotype_test(request.POST)
        #У нас есть форма и объект персона
        if form.is_valid():
            mbti_type = ''
            dichotomys = {'extraversion': 0, 'introversion': 0, 'sensing': 0, 'intuition': 0, 'thinking': 0,
                      'feeling': 0, 'judging': 0, 'perceiving': 0}
            for num in range(len(form.fields.keys())):
                dichotomys[form.cleaned_data['choice_' + str(num + 1)]] += 1

            mbti_type += 'E' if dichotomys['extraversion'] > dichotomys['introversion'] else  'I'
            mbti_type += 'S' if dichotomys['sensing'] > dichotomys['intuition'] else 'N'
            mbti_type += 'T' if dichotomys['thinking'] > dichotomys['feeling'] else 'F'
            mbti_type += 'J' if dichotomys['judging'] > dichotomys['perceiving'] else 'P'
            pers.social_type = mbti_type
            pers.save()
            #socionic_type = get_object_or_404(Socionic_type, symbol_dif = mbti_type)
            return HttpResponseRedirect(reverse('sociotypetest:sociotest_result', args=(pers.id,)))
            #return render(request, 'sociotypetest/sociotest_result.html',
            #              {'pers': pers, 'dichotomys': dichotomys,
            #               'mbti_type': mbti_type, 'socionic_type': socionic_type}, )
    else:
        form = sociotype_test()
        return render(request, 'sociotypetest/sociotest.html', {'form': form, 'pers' : pers})

def sociotest_result(request, personal_id):
    pers = get_object_or_404(Personal_info, pk = personal_id)
    social_type_all = Socionic_type.objects.all.get()
    if pers.social_type:
        socionic_type = get_object_or_404(Socionic_type, symbol_dif=pers.social_type)
    return render(request, 'sociotypetest/sociotest_result.html', {'pers' : pers, 'socionic_type': socionic_type})



