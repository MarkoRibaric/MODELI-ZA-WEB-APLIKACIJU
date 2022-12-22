from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from main.models import Party, Candidate, VotingPlace, Voter, Ballot


def homepage(request):
    return render(request, 'base_generic.html')

class CandidateList(ListView):
    model = Candidate

class PartyList(ListView):
    model = Party

class VotingPlaceList(ListView):
    model = VotingPlace

class VoterList(ListView):
    model = Voter

class BallotList(ListView):
    model = Ballot


class VotingplaceVoterList(ListView):
    template_name = "voter_list.html"

    def get_queryset(self):
        print(self.kwargs)
        self.voting_place = get_object_or_404(VotingPlace, name=self.kwargs['voting_place'])

        return Voter.objects.filter(voting_place=self.voting_place)