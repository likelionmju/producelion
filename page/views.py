from django.shortcuts import render
from vote.models import VoteList
from vote.urls import urlpatterns
# Create your views here.

def home(request):
  return render(request, "home.html")

