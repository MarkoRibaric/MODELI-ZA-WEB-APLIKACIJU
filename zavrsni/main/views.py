from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from main.models import Party, Candidate, VotingPlace, Voter, Ballot
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

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

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def add_party(request):
    submitted = False
    if request.method == "POST":
        form = PartyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = PartyForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_party.html', {'form':form, 'submitted':submitted})

def add_candidate(request):
    submitted = False
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = CandidateForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_candidate.html', {'form':form, 'submitted':submitted})

def add_votingplace(request):
    submitted = False
    if request.method == "POST":
        form = VotingPlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = VotingPlaceForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_votingplace.html', {'form':form, 'submitted':submitted})


def add_voter(request):
    submitted = False
    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = VoterForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_voter.html', {'form':form, 'submitted':submitted})

def add_ballot(request):
    submitted = False
    if request.method == "POST":
        form = BallotForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = BallotForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_ballot.html', {'form':form, 'submitted':submitted})




def delete_ballot(request, id_of_ballot):
    ballot = get_object_or_404(Ballot, pk=id_of_ballot)


 
    context = {'ballot': ballot}    
    
    if request.method == 'GET':
        return render(request, 'main/ballot_confirm_delete.html',context)
    elif request.method == 'POST':
        ballot.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect("ballot")

def edit_candidate(request, OIB):
    candidate = get_object_or_404(Candidate, OIB=OIB)
    
    if request.method == 'GET':
        context = {'form': CandidateForm(instance=candidate), 'OIB': OIB}
        return render(request,'main/edit_candidate.html',context)
    elif request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            messages.success(request, 'The Candidate has been updated successfully.')
            return redirect('candidate')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'main/edit_candidate.html',{'form':form})