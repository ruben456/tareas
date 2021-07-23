from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsUserOrReadOnly
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework import filters

#Task
class ListTask(generics.ListCreateAPIView):
    """ Vista para listar y crear tareas """
    search_fields = ['description']
    filter_backends = (filters.SearchFilter,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    """ Vista para ver detalle, actualizar y eliminar tareas """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, IsUserOrReadOnly)
