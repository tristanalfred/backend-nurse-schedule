from django.http import HttpResponse
from django.http import JsonResponse

from schedule.models import Member, Team

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def member_list(request):
    
    team = request.GET.get('team')
    if team:
        data = list(Member.objects.filter(team=team).values())
    else:
        data = list(Member.objects.values())        
    return JsonResponse({'data': data})


def team_list(request):
    data = list(Team.objects.values())
    return JsonResponse({'data': data})


def team_detail(request, id):
    data_team = Team.objects.values().get(id=id)
    data_members = list(Member.objects.filter(team__id=id).values('id', 'first_name', 'last_name'))
    
    data_team['members'] = data_members
    
    return JsonResponse({'data': data_team})
