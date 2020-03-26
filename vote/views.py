from django.shortcuts import render
from account.models import Profile
from .models import VoteList
from django.contrib.auth.models import User

def vote(request):
  picks = Profile.objects
  return render(request, "vote/list.html",{'picks':picks})

def complete(request):
    nowuser = VoteList.objects.filter(user=request.user)
    if not nowuser:
      myvote = VoteList()
      myvote.user = request.user
      myvote.myname = request.user.username
      myvote.name = request.POST.get('pick')
      myvote.votenum += 1
      myvote.save()
    else:
      obj = VoteList.objects.get(user = request.user)
      obj.name = request.POST.get('pick')
      obj.votenum += 1
      obj.save()
    return render(request,"vote/complete.html")
