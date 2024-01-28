# En gestorpass/views.py
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response

from .forms import PasswordEntryForm
from .models import PasswordEntry
from .serializers import PasswordEntrySerializer

from rest_framework.views import APIView

from rest_framework import generics


class PasswordEntryListCreateView(generics.ListCreateAPIView):
    queryset = PasswordEntry.objects.all()
    serializer_class = PasswordEntrySerializer

class PasswordEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PasswordEntry.objects.all()
    serializer_class = PasswordEntrySerializer

class PasswordEntryViewSet(viewsets.ModelViewSet):
    queryset = PasswordEntry.objects.all()
    serializer_class = PasswordEntrySerializer

    def passwordentry_delete(self, request, pk=None):
        password_entry = self.get_object()
        
        if request.method == 'POST':
            password_entry.delete()
            return redirect('passwordentry_list')

        return render(request, 'gestorpass/passwordentry_delete.html', {'password_entry': password_entry})

    def passwordentry_list(self, request):
        password_entries = PasswordEntry.objects.all()
        return render(request, 'gestorpass/passwordentry_list.html', {'password_entries': password_entries})

    def passwordentry_detail(self, request, entry_id):
        password_entry = PasswordEntry.objects.get(id=entry_id)
        return render(request, 'gestorpass/passwordentry_detail.html', {'password_entry': password_entry})

    def passwordentry_create(self, request):
        if request.method == 'POST':
            form = PasswordEntryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('passwordentry_list')
        else:
            form = PasswordEntryForm()

        return render(request, 'gestorpass/passwordentry_form.html', {'form_title': 'Crear Contraseña', 'form': form})

    def passwordentry_update(self, request, entry_id):
        password_entry = PasswordEntry.objects.get(id=entry_id)

        if request.method == 'POST':
            form = PasswordEntryForm(request.POST, instance=password_entry)
            if form.is_valid():
                form.save()
                return redirect('passwordentry_list')
        else:
            form = PasswordEntryForm(instance=password_entry)

        return render(request, 'gestorpass/passwordentry_form.html', {'form_title': 'Editar Contraseña', 'form': form})
