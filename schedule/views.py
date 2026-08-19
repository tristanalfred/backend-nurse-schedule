from rest_framework import viewsets
from rest_framework.decorators import action

from schedule.models import Member, Shift, ShiftPreference, Team
from schedule.serializers import TeamSerializer, MemberSerializer, ShiftSerializer, ShiftPreferenceSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
    @action(detail=True, methods=["get"])
    def shifts(self, request, pk=None):
        member = self.get_object()
        shifts = Shift.objects.filter(member=member)
        serializer = ShiftSerializer(shifts, many=True)
        return Response(serializer.data)


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ShiftPreferenceViewSet(viewsets.ModelViewSet):
    queryset = ShiftPreference.objects.all()
    serializer_class = ShiftPreferenceSerializer
