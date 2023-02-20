from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import *

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class PartyForm(forms.ModelForm):
    
    class Meta:
        model = Party
        fields = ('name', 'abbreviation')
    

class CandidateForm(forms.ModelForm):
    
    class Meta:
        model = Candidate
        fields = ('name', 'OIB', 'age', 'party')

class VotingPlaceForm(forms.ModelForm):
    
    class Meta:
        model = VotingPlace
        fields = ('name', 'address', 'open_at', 'close_at')

class VoterForm(forms.ModelForm):
    
    class Meta:
        model = Voter
        fields = ('name', 'OIB', 'age', 'voting_place')

class BallotForm(forms.ModelForm):
    
    class Meta:
        model = Ballot
        fields = ('voter', 'time_of_ballot', 'id_of_ballot', 'voted_for')


