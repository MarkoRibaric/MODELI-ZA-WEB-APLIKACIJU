import factory
import random
from factory.django import DjangoModelFactory
from .models import Party, Candidate, VotingPlace, Voter, Ballot

class PartyFactory(DjangoModelFactory):
    class Meta:
        model = Party

    name = factory.Faker("company")
    abbreviation = factory.Faker("pystr", max_chars=4)

class CandidateFactory(DjangoModelFactory):
    class Meta:
        model = Candidate
    name = factory.Faker("name")
    OIB = factory.Faker("random_int", min=1000000000000, max=9999999999999)
    age = factory.Faker("random_int", min=18, max=65)
    @factory.post_generation
    def party(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for oneparty in random.sample(extracted, random.randint(1, 3)):
                self.party.add(oneparty)
    


class VotingPlaceFactory(DjangoModelFactory):
    class Meta:
        model = VotingPlace

    name = factory.Faker("word")
    address = factory.Faker("address")
    open_at = factory.Faker("time", pattern="%H:%M:%S")
    close_at = factory.Faker("time", pattern="%H:%M:%S")

class VoterFactory(DjangoModelFactory):
    class Meta:
        model = Voter
    name = factory.Faker("name")
    OIB = factory.Faker("random_int", min=1000000000000, max=9999999999999)
    age = factory.Faker("random_int", min=18, max=65)
    voting_place = factory.Iterator(VotingPlace.objects.all())

class BallotFactory(DjangoModelFactory):
    class Meta:
        model = Ballot
    voter = factory.Iterator(Voter.objects.all())
    time_of_ballot = factory.Faker("time", pattern="%H:%M:%S")
    id_of_ballot = factory.Faker("pystr", max_chars=10)
    voted_for = factory.Iterator(Candidate.objects.all())
