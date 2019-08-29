from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from .models import Journal

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login_custom'))
    journals = Journal.objects.all().filter(author_id=request.user.id)
    return render(request, 'journal/index.html', {'journals': journals})

def add_journal(request):
    title = request.POST['title']
    body = request.POST['body']
    try:
        Journal.objects.create(title=title, body=body, author_id=request.user)
    except KeyError:
        render(request, "journal/error.html", {"message": "Error Adding a Journal"})
    return HttpResponseRedirect(reverse('journal:index'))

def delete_journal(request, journal_id):
    try:
        journal = Journal.objects.get(pk=journal_id)
    except Journal.DoesNotExist:
        raise Http404("Journal does not exist.")
    journal.delete()
    return HttpResponseRedirect(reverse('journal:index'))

def edit_journal(request, journal_id):
    try:
        journal = Journal.objects.get(pk=journal_id)
    except Journal.DoesNotExist:
        raise Http404("Journal does not exist.")
    if request.method == "POST":
        journal.title = request.POST['title']
        journal.body = request.POST['body']
        journal.save()
        return HttpResponseRedirect(reverse('journal:index'))
    context = {
        'journal': journal
    }
    return render(request, "journal/edit.html", context)
