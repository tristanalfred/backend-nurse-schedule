from django.db.models import F
from django.http import HttpResponse
from django.http import JsonResponse

from schedule.models import Member, Shift, ShiftPreference, Team

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def team_list(request):
    data = list(Team.objects.values())
    return JsonResponse({'data': data})


def team_detail(request, id):
    data_team = Team.objects.values().get(id=id)
    data_members = list(Member.objects.filter(team__id=id).values('id', 'first_name', 'last_name'))
    
    data_team['members'] = data_members
    
    return JsonResponse({'data': data_team})


def member_list(request):
    
    team = request.GET.get('team')
    if team:
        data = list(Member.objects.filter(team=team).values())
    else:
        data = list(Member.objects.values())        
    return JsonResponse({'data': data})


def member_shift_list(request, id):
    shift_type = request.GET.get('type', None)
    # prefered_shifts = list(Member.objects.filter(id=id).values_list('shift_preferences'))
    prefered_shifts = list(
        ShiftPreference.objects
        .annotate(name=F('shift__name'))
        .annotate(long_name=F('shift__long_name'))
        .filter(member__id=id).values('name', 'long_name', 'note', 'weekday')
    )
    return JsonResponse({'data': prefered_shifts})


def shift_list(request):
    data = list(Shift.objects.values())
    return JsonResponse({'data': data})
