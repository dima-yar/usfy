from django.urls import path
from . import views

app_name = 'local_records'

urlpatterns = [
    path('<int:pk>/', views.region, name="region")
]
