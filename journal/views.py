from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Journal

# Create your views here.
def index(request):
    journals = Journal.objects.all()
    # return HttpResponse("My app is running. Journal is up")
    return render(request, 'journal/index.html', {'journals': journals})

def add_journal(request):
    title = request.POST['title']
    body = request.POST['body']
    try:
        Journal.objects.create(title=title, body=body)
    except KeyError:
        render(request, "journal/error.html", {"message": "Error Adding a Journal"})
    return HttpResponseRedirect(reverse('journal:index'))

def delete_journal(request, journal_id):
    try:
        journal = Journal.objects.get(pk=journal_id)
    except Journal.DoesNotExist:
        raise Http404("Flight does not exist.")
    journal.delete()
    return HttpResponseRedirect(reverse('journal:index'))