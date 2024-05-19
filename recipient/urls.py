from django.urls import path

from recipient.apps import RecepientConfig
from recipient.views import (RecipientListView, RecipientCreateView, RecipientDeleteView,
                             RecipientDetailView, RecipientUpdateView)

app_name = RecepientConfig.name

urlpatterns = [
    path('', RecipientListView.as_view(), name='list'),
    path('create/', RecipientCreateView.as_view(), name='create'),
    path('<int:pk>/', RecipientDetailView.as_view(), name='view'),
    path('<int:pk>/update/', RecipientUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', RecipientDeleteView.as_view(), name='delete'),
]