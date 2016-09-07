from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader

from .models import Booker


def invite_home(request):
    booking = Booker.objects.all()
    template = loader.get_template('emailsadd/invite_home.html')
    context = {
        'booking': booking,
    }
    return HttpResponse(template.render(context, request))


def user_invitation(request):
    booking = Booker.objects.all()
    template = loader.get_template('emailsadd/user_invitation.html')
    context = {
        'booking': booking,
    }
    return HttpResponse(template.render(context, request))


def user_reminder(request):
    booking = Booker.objects.all()
    template = loader.get_template('emailsadd/user_reminder.html')
    context = {
        'booking': booking,
    }
    return HttpResponse(template.render(context, request))


def invite_survey(request):
    booking = Booker.objects.all()
    template = loader.get_template('emailsadd/invite_survey.html')
    context = {
        'booking': booking,
    }
    return HttpResponse(template.render(context, request))


@login_required
def postform(request):
    mycompany_name = request.POST.get("company_name")
    mymanager_name = request.POST.get("manager_name")
    myevent_name = request.POST.get("event_name")
    mylocation = request.POST.get("location")
    myfromtime = request.POST.get("from_time")
    mytotime = request.POST.get("to_time")
    mydate = request.POST.get("date")
    myparticipants_number = request.POST.get("participants_number")
    myparticipants = request.POST.get("participants_email")

    new_activity = Booker.objects.create(company_name=mycompany_name, manager_name=mymanager_name,event_name=myevent_name, location=mylocation,from_time=myfromtime,to_time=mytotime,
                                         date=mydate,participants_number=myparticipants_number,participants_email=myparticipants)
    # , duration = myduration
    new_activity.save()
    return redirect('user_invitation')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/emailsadd/")
        else:
            form = UserCreationForm()
        return render(request, "registration/register.html", {
            'form': form,
        })
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
