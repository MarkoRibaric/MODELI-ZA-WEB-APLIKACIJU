from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from main.views import *
import factory


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        print(resolve(url))

        self.assertEquals(resolve(url).func, homepage)

    def test_candidate_url_is_resolved(self):
        url = reverse('candidate')

        self.assertEquals(resolve(url).func.view_class, CandidateList)

    def test_party_url_is_resolved(self):
        url = reverse('party')

        self.assertEquals(resolve(url).func.view_class, PartyList)

    def test_votingplace_url_is_resolved(self):
        url = reverse('votingplace')

        self.assertEquals(resolve(url).func.view_class, VotingPlaceList)
    
    def test_voter_url_is_resolved(self):
        url = reverse('voter')

        self.assertEquals(resolve(url).func.view_class, VoterList)

    def test_ballot_url_is_resolved(self):
        url = reverse('ballot')

        self.assertEquals(resolve(url).func.view_class, BallotList)
    
    def test_register_url_is_resolved(self):
        url = reverse('register')

        self.assertEquals(resolve(url).func, register_request)
    def test_addparty_url_is_resolved(self):
        url = reverse('addparty')

        self.assertEquals(resolve(url).func, add_party)
    def test_addcandidate_url_is_resolved(self):
        url = reverse('addcandidate')

        self.assertEquals(resolve(url).func, add_candidate)
    def test_addvotingplace_url_is_resolved(self):
        url = reverse('addvotingplace')

        self.assertEquals(resolve(url).func, add_votingplace)
    def test_addvoter_url_is_resolved(self):
        url = reverse('addvoter')

        self.assertEquals(resolve(url).func, add_voter)
    def test_addballot_url_is_resolved(self):
        url = reverse('addballot')

        self.assertEquals(resolve(url).func, add_ballot)
    
    

class TestModels(TestCase):

    def setUp(self):
        self.votingplace1 = VotingPlace.objects.create(
            name = "ALBAQUERKE",
            address = "ALBAQEUERKE DISTRICT",
            open_at = "7:52",
            close_at = "9:56",
        )
        self.voter1 = Voter.objects.create(
            name = "Marko",
            OIB = "73465346",
            age = "42",
            voting_place = self.votingplace1
        )
        self.party1 = Party.objects.create(
            name = "najbolji party",
            abbreviation = "PARTY"
        )

        self.candidate1 = Candidate.objects.create(
            name = "Miroslav",
            OIB = "63463463",
            age = "63",
        )
        self.candidate1.party.add(self.party1)

        self.ballot1 = Ballot.objects.create(
            voter = self.voter1,
            time_of_ballot = "7:35",
            id_of_ballot = "aergae",
            voted_for = self.candidate1
        )





    def test_votingplace(self):
        self.assertEquals(self.votingplace1.name, "ALBAQUERKE")
    def test_voter(self):
        self.assertEquals(self.voter1.name, "Marko")
    def test_party(self):
        self.assertEquals(self.party1.name, "najbolji party")
    def test_candidate(self):
        self.assertEquals(self.candidate1.name, "Miroslav")
    def test_ballot(self):
        self.assertEquals(self.ballot1.voter, self.voter1)
    def test_candidateparty(self):
        self.assertEquals(self.candidate1.party.all()[0], self.party1)
    

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.candidate = reverse('candidate')
        self.party = reverse('party')
        self.votingplace = reverse('votingplace')
        self.voter = reverse('voter')
        self.ballot = reverse('ballot')
        self.register = reverse('register')
        self.party1 = Party.objects.create(
            name = 'Markov Party',
            abbreviation = 'ADBC',
        )

    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')

    def test_project_candidate_GET(self):
        client = Client()

        response = client.get(self.candidate)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/candidate_list.html')
    
    def test_project_party_GET(self):
        client = Client()

        response = client.get(self.party)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/party_list.html')

    def test_project_votingplace_GET(self):
        client = Client()

        response = client.get(self.votingplace)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/votingplace_list.html')

    def test_project_voter_GET(self):
        client = Client()

        response = client.get(self.voter)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/voter_list.html')

    def test_project_ballot_GET(self):
        client = Client()

        response = client.get(self.ballot)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/ballot_list.html')

    

    def test_project_register_GET(self):
        client = Client()

        response = client.get(self.register)
        self.assertEquals(response.status_code, 200)



