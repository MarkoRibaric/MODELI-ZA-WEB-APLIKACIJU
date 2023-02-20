from django.db import models

class Party(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    OIB = models.PositiveIntegerField(primary_key=True)
    age = models.PositiveIntegerField()
    party = models.ManyToManyField(Party, related_name="candidates")
    def __str__(self):
        return self.name
    def party_names(self):
        return ', '.join([a.abbreviation for a in self.party.all()])
    party_names.short_description="Parties: "

class VotingPlace(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=200)
    open_at = models.TimeField()
    close_at = models.TimeField()
    
    def __str__(self):
        return self.name

class Voter(models.Model):
    name = models.CharField(max_length=100)
    OIB = models.PositiveIntegerField(primary_key=True)
    age = models.PositiveIntegerField()
    voting_place = models.ForeignKey(VotingPlace, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Ballot(models.Model):
    voter = models.OneToOneField(Voter, on_delete=models.CASCADE)
    time_of_ballot = models.TimeField()
    id_of_ballot = models.CharField(max_length=10, primary_key=True)
    voted_for = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    def __str__(self):
        return f'Ballot for {self.voter.name}'

