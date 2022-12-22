from django.contrib import admin
from main.models import Party, Candidate, VotingPlace, Voter, Ballot
# Register your models here.

models_list = [Party, Candidate, VotingPlace, Voter, Ballot]

admin.site.register(models_list)