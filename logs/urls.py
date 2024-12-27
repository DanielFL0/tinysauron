from django.urls import path
from . import views

app_name = "logs"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:log_id>/", views.detail, name="detail"),
]