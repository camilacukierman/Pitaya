import datetime
from email.mime.image import MIMEImage

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.db.models import Avg
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template

from .forms import ImageUploadForm
from .models import Booker,Newsletter,Survey


@login_required
def invite_home(request):
    booking = None
    if request.user:
        booking = Booker.objects.filter(user_id=str(request.user.id))
    template = get_template('emailsadd/invite_home.html')

    context = {
        'booking': booking,
        'number_of_bookings': len(booking),
        'mode': "login"

    }
    return HttpResponse(template.render(context, request))


@login_required
def events(request):
    booking = None
    if request.user:
        booking = Booker.objects.filter(user_id=str(request.user.id))
    else:
        return redirect('/')
    template = get_template('emailsadd/events.html')

    context = {
        'booking': booking.order_by('-date'),
        'number_of_bookings': len(booking),
    }
    return HttpResponse(template.render(context, request))


@login_required
def event_status(request, eid):
    booking = Booker.objects.get(id=eid)
    participants = Newsletter.objects.filter(booker_id=booking.id)
    surveys = Survey.objects.filter(booker_id=booking.id)

    survey_a1_avg = surveys.aggregate(Avg('a1'))
    survey_a2_avg = surveys.aggregate(Avg('a2'))
    survey_a3_avg = surveys.aggregate(Avg('a3'))

    template = get_template('emailsadd/event_status.html')
    context = {
        'booking': booking,
        'participants': participants,
        'surveys' : surveys,
        'a1_avg' : survey_a1_avg['a1__avg'],
        'a2_avg': survey_a2_avg['a2__avg'],
        'a3_avg': survey_a3_avg['a3__avg'],
    }
    return HttpResponse(template.render(context, request))


@login_required
def user_invitation(request):
    booking = Booker.objects.get(pk=request.session.get('new_activity_id'))
    print(booking.event_name)
    newsletter = Newsletter.objects.get(pk=request.session.get('new_mail_id'))
    template = get_template('emailsadd/user_invitation.html')
    context = {
        'booking': booking,
        'invitee': newsletter,
        'not_email': True
    }
    return HttpResponse(template.render(context, request))


@login_required
def user_reminder(request):
    booking = Booker.objects.all()
    template = get_template('emailsadd/user_reminder.html')
    context = {
        'booking': booking,
    }
    return HttpResponse(template.render(context, request))


@login_required
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

    myfromtime = datetime.datetime.strptime(mydate +' ' + myfromtime, "%Y-%m-%d %H:%M")
    mytotime = datetime.datetime.strptime(mydate +' ' + mytotime, "%Y-%m-%d %H:%M")

    new_activity = Booker.objects.create(manager_name=mymanager_name,
                                         event_name=myevent_name, location=mylocation, from_time= datetime.datetime(myfromtime.year, myfromtime.month, myfromtime.day, myfromtime.hour, myfromtime.minute),
                                         to_time=datetime.datetime(mytotime.year, mytotime.month, mytotime.day, mytotime.hour, mytotime.minute),
                                         date=datetime.datetime.strptime(mydate, "%Y-%m-%d").date(), event_description=myevent_description,
                                         manager_message=mymanager_message)

    numberOfEmails = int(request.POST.get("participants_number"))

    save_image(new_activity, request)

    new_activity.save()

    for i in range(0, numberOfEmails):
        new_mail = init_newsletter(new_activity, request, "participants_name" + str(i), "participants_email" + str(i))
        request.session['new_mail_id'] = new_mail.id
        if new_mail:
            send_email(new_mail, new_activity)

    request.session['new_activity_id'] = new_activity.id

    return redirect(reverse('user_invitation'))


def init_newsletter(new_activity, request, participants_name, participants_email):
    myparticipants_name = request.POST.get(participants_name)
    myparticipants_email = request.POST.get(participants_email)
    if myparticipants_email:
        new_mail = Newsletter.objects.create(booker_id=new_activity, participants_name=myparticipants_name,
                                             participants_email=myparticipants_email)
        new_mail.save()
        return new_mail
    else:
        return None



def save_image(new_activity, request):
    # saving the pic for the event
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_activity.pic = form.cleaned_data['image']
            new_activity.save()
        else:
            print (form.errors)


def send_email(new_mail, new_activity):
    print('entramos na func email')
    try:
        plaintext = get_template('emailsadd/email.txt')
        htmly = get_template('emailsadd/user_invitation.html')
        d = Context({'booking': new_activity, "invitee": new_mail})
        subject, from_email, to = new_activity.event_name, 'donotreplypitaya@gmail.com', new_mail.participants_email
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        # settings.STATIC_ROOT + "pic_folder/" + new_activity.pic
        image_file = open(new_activity.pic.path, 'rb')
        msg_image = MIMEImage(image_file.read())
        image_file.close()
        msg_image.add_header('Content-ID', '<image1>')
        msg.mixed_subtype = 'related'
        msg.attach(msg_image)
        msg.send()
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)





def approved(request, pid,approved):
    approvedParticipant = Newsletter.objects.get(id=pid)
    approvedParticipant.approved = approved
    approvedParticipant.save()
    template = get_template('emailsadd/thankyou.html')
    context = {
        'invitee': approvedParticipant,
    }
    return HttpResponse(template.render(context, request))

def survey(request, pid):
    template = get_template('emailsadd/survey.html')
    context = {
        "pid": pid,
    }
    return HttpResponse(template.render(context, request))



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
        'mode': "register"
    })


def event_feedback(request):
    booking = Booker.objects.get(pk=request.session.get('new_activity_id'))
    template = get_template('emailsadd/event_feedback.html')
    context = {
        'booking': booking,
        # 'image_src': request.session.get('myimage_preview')
    }
    return HttpResponse(template.render(context, request))


def survey_complete(request, pid):
    template = get_template('emailsadd/survey_complete.html')
    context = {
        "pid": pid,
    }
    return HttpResponse(template.render(context, request))


def postsurvey(request):
    pid = request.POST.get("pid")
    survey_participant = Newsletter.objects.get(id=pid)
    answer_one = request.POST.get("a1")
    answer_two = request.POST.get("a2")
    answer_three = request.POST.get("a3")
    answer_four = request.POST.get("a4")
    new_survey = Survey.objects.create(participant_ref_id = survey_participant.id,a1=answer_one, a2=answer_two, a3=answer_three, a4=answer_four)
    new_survey.booker_id = survey_participant.booker_id.id


    if survey_participant.answer_survey == True:
        template = get_template('emailsadd/thankyou.html')

    else:
        survey_participant.answer_survey = True
        survey_participant.save()
        new_survey.save()
        template = get_template('emailsadd/thankyou.html')
    context = {
        'invitee': survey_participant,
    }
    return HttpResponse(template.render(context, request))


