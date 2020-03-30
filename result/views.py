from django.shortcuts import render,redirect
from vote.models import VoteList

def result(request):
    votes = VoteList.objects
    return render(request,'result/result.html',{'votes':votes})

def beforeteam(request):
    votes = VoteList.objects.all()
    for vote in votes:
        vote.lastteam = vote.team
        vote.save()
    return redirect('result')
    