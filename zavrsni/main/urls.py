from django.urls import path, include
from main.views import *


urlpatterns = [
    path("", homepage, name="homepage"),
    path("candidate", CandidateList.as_view(), name="candidate"), 
    path("party", PartyList.as_view(), name="party"),
    path("votingplace", VotingPlaceList.as_view(), name="votingplace"),
    path("voter", VoterList.as_view(), name="voter"),
    path("ballot", BallotList.as_view(),  name="ballot"),
    path('register/', register_request, name='register'),
    path('add_party', add_party, name="addparty"),
    path('add_candidate', add_candidate, name="addcandidate"),
    path('add_votingplace', add_votingplace, name="addvotingplace"),
    path('add_voter', add_voter, name="addvoter"),
    path('add_ballot', add_ballot, name="addballot"),
    path("<voting_place>", VotingplaceVoterList.as_view(), name="votingplaces"),
    path('ballot/delete/<id_of_ballot>/', delete_ballot, name='ballot-delete'),
    path('candidate/edit/<int:OIB>/', edit_candidate, name='candidate-edit')
]
