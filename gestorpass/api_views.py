# En gestorpass/api_views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PasswordEntry  # Asegúrate de que esta importación sea correcta
from .serializers import PasswordEntrySerializer  # Asegúrate de que esta importación sea correcta


class PasswordEntryViewSet(viewsets.ModelViewSet):
    queryset = PasswordEntry.objects.all()
    serializer_class = PasswordEntrySerializer

    @action(detail=True, methods=['get'])
    def get_notes(self, request, pk=None):
        password_entry = self.get_object()
        notes = password_entry.notes
        return Response({'notes': notes})

    # Puedes agregar más acciones personalizadas según tus necesidades