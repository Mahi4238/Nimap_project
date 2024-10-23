from rest_framework import viewsets
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def assign_users(self, request, pk=None):
        project = self.get_object()
        users = request.data.get('users')
        for user in users:
            project.users.add(user['id'])
        return Response({'status': 'users assigned'})
