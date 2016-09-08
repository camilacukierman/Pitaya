from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template

from .models import Booker
from .models import Newsletter


def invite_home(request):
    booking = Booker.objects.all()
    template = get_template('emailsadd/invite_home.html')
    context = {
        'booking': booking,

    }
    return HttpResponse(template.render(context, request))


def user_invitation(request):
    booking = Booker.objects.get(pk = request.session.get('new_activity_id'))
    template = get_template('emailsadd/user_invitation.html')
    context = {
        'booking': booking,
        # 'image_src': request.session.get('myimage_preview')
    }
    return HttpResponse(template.render(context, request))


def user_reminder(request):
    booking = Booker.objects.all()
    template = get_template('emailsadd/user_reminder.html')
    context = {
        'booking': booking,
    }
    return HttpResponse(template.render(context, request))


def invite_survey(request):
    booking = Booker.objects.all()
    template = get_template('emailsadd/invite_survey.html')
    context = {
        'booking': booking,
    }
    return HttpResponse(template.render(context, request))


@login_required
def postform(request):
    mymanager_name = request.POST.get("manager_name")
    myevent_name = request.POST.get("event_name")
    mylocation = request.POST.get("location")
    myfromtime = request.POST.get("from_time")
    mytotime = request.POST.get("to_time")
    mydate = request.POST.get("date")
    myevent_description = request.POST.get("event_description")
    mymanager_message = request.POST.get("manager_message")
    myimage_preview= request.POST.get("image_preview")
    new_activity = Booker.objects.create(manager_name=mymanager_name,
                                         event_name=myevent_name, location=mylocation, from_time=myfromtime,
                                         to_time=mytotime,
                                         date=mydate, event_description=myevent_description,
                                         manager_message=mymanager_message)

    numberOfEmails = int(request.POST.get("participants_number"))

    new_mail = init_newsletter(new_activity, request, "participants_name", "participants_email")
    email = EmailMessage(myevent_name, myevent_description, to=[new_mail.participants_email])
    email.send()
    send_email(new_mail, new_activity)
    for i in range(1, numberOfEmails):
        new_mail = init_newsletter(new_activity, request, "participants_name" + str(i), "participants_email" + str(i))
        email = EmailMessage(myevent_name, myevent_description, to=[new_mail.participants_email])
        email.send()
        send_email(new_mail, new_activity)

    new_activity.save()

    request.session['new_activity_id'] = new_activity.id
    # request.session['myimage_preview'] = myimage_preview
    return redirect('user_invitation')


def send_email(new_mail, new_activity):
    plaintext = get_template('emailsadd/email.txt')
    htmly = get_template('emailsadd/user_invitation.html')

    d = Context({'username': 'Tzvi'})

    subject, from_email, to = new_activity.event_name, 'pitayaproject@gmail.com', new_mail.participants_email
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def init_newsletter(new_activity, request, participants_name, participants_email):
    myparticipants_name = request.POST.get(participants_name)
    myparticipants_email = request.POST.get(participants_email)
    new_mail = Newsletter.objects.create(booker_id=new_activity, participants_name=myparticipants_name,
                                         participants_email=myparticipants_email)
    new_mail.save()
    return new_mail


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
