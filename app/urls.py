from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    path("", views.home, name="home"),
    path("get_processor_data/", views.processor_create, name="get_processor_data"),
    path("processors/", views.processors, name="processors"),
    path("pc_builder/", views.pc_builder, name="pc_builder")
]