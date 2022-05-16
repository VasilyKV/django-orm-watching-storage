from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .models import get_duration
from .models import is_visit_long
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits_orm = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in non_closed_visits_orm:
        duration = get_duration(visit)
        visit_details = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': duration,
            'is_strange': is_visit_long(duration, minutes=60)
        }
        non_closed_visits.append(visit_details)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
