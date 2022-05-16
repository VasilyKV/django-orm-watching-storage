from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .models import get_duration
from .models import is_visit_long
from django.utils.timezone import localtime


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in active_visits:
        duration = get_duration(visit)
        temp_dict = {
            'who_entered': f'{visit.passcard.owner_name}',
            'entered_at': f'{localtime(visit.entered_at)}',
            'duration': f'{duration}',
            'is_strange': f'{is_visit_long(duration, minutes=60)}'
        }
        non_closed_visits.append(temp_dict)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
