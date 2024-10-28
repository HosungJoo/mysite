from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #views에 index함수 실행
]