from django.urls import path, include
from main.views import *


urlpatterns = [
    path("", homepage, name="homepage"),
    path("candidate", CandidateList.as_view()), 
    path("party", PartyList.as_view()),
    path("votingplace", VotingPlaceList.as_view()),
    path("voter", VoterList.as_view()),
    path("ballot", BallotList.as_view()),
    path("<voting_place>", VotingplaceVoterList.as_view())
]