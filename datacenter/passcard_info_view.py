from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .models import get_duration
from .models import is_visit_long
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits_orm = Visit.objects.filter(passcard__passcode=passcode)
    this_passcard_visits = []
    for visit in this_passcard_visits_orm:
        duration = get_duration(visit)
        visit_details = {
                'entered_at': localtime(visit.entered_at),
                'duration': duration,
                'is_strange': is_visit_long(duration, minutes=60)
            }
        this_passcard_visits.append(visit_details)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
