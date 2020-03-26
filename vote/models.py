from django.db import models
from django.contrib.auth.models import User

class VoteList(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    myname = models.CharField(max_length=10,blank=True)
    name = models.CharField(max_length=10,blank=True)
    votenum = models.IntegerField(default=0)
    def __str__(self):
        return self.myname