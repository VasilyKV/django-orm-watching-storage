from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .models import get_duration
from .models import is_visit_long
from django.utils.timezone import localtime

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    person_visits = Visit.objects.filter(passcard__passcode=passcode)
    this_passcard_visits = []
    for visit in person_visits:
        duration = get_duration(visit)
        temp_dict = {
                'entered_at': f'{localtime(visit.entered_at)}',
                'duration': f'{duration}',
                'is_strange': f'{is_visit_long(duration, minutes=60)}'
            }
        this_passcard_visits.append(temp_dict)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
