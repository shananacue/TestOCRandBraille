
from django.contrib import admin
from django.urls import path
#from . import views
from .views import TestsView, TestDetailView, AddTestView

urlpatterns = [
    path('', TestsView.as_view(), name="test"),
    path('tests/<int:pk>', TestDetailView.as_view(), name="test-details"),
    #pk->primary key... unique id number assigned to new database record entry
    path('add_test/', AddTestView.as_view(), name = 'add-test')

]