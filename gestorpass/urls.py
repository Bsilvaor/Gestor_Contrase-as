from django.urls import path, include
from rest_framework import routers
from .views import PasswordEntryViewSet
from .views import PasswordEntryListCreateView, PasswordEntryDetailView

router = routers.DefaultRouter()
router.register(r'passwords', PasswordEntryViewSet, basename='passwords')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/viewpasswords/', PasswordEntryViewSet.as_view({'get': 'list', 'post': 'create'}), name='passwords-list'),
    path('api/passwords/', PasswordEntryListCreateView.as_view(), name='password-entry-list-create'),
    path('api/passwords/<int:pk>/', PasswordEntryDetailView.as_view(), name='password-entry-detail'),
]
