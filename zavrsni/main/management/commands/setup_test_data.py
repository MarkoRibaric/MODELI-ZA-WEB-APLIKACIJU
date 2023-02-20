from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import Party, Candidate, VotingPlace, Voter, Ballot
from main.factory import PartyFactory, CandidateFactory, VotingPlaceFactory, VoterFactory, BallotFactory

PARTY = 20
CANDIDATE = 25
VOTING_PLACE = 15
VOTER = 100
BALLOT = 100
class Command(BaseCommand):
    help = "This command generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Deleting old data...")
        models = [Party, Candidate, VotingPlace, Voter, Ballot]
        for model in models:
            model.objects.all().delete()

        self.stdout.write("Creating new data...")
        for i in range(VOTING_PLACE):
            VotingPlaceFactory()
        
        for i in range(VOTER):
            VoterFactory()
        
        

        parties=[]
        for i in range(PARTY):
            parties.append(PartyFactory())

        for i in range(CANDIDATE):
            CandidateFactory.create(party=parties)
        
        for i in range(BALLOT):
            BallotFactory()
