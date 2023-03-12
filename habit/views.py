
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from habit.models import Habit
from habit.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get(self, request):
        output = [
            {
                "award": output.award,
                "action": output.action
            } for output in Habit.objects.all()
        ]
        return Response(output)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#class HabitView(APIView):
#    def get(self, request):
#           output = [
#               {
#                   "award": output.award,
#                   "action": output.action
#               } for output in Habit.objects.all()
#           ]
#           return Response(output)
#
#
#    def post(self, request):
#        serializer = HabitSerializer(data=request.data)
#        if serializer.is_valid(raise_exception=True):
#            serializer.save()
#            return Response(serializer.data)