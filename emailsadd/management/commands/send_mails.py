import datetime
import os
from email.mime.image import MIMEImage

from django import db
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template import Context
from django.template.loader import get_template

from emailsadd.models import Booker, Newsletter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pitaya.settings")


def send_email_reminder(event_name, participant_email_reminder, participant_name_reminder, event_pic):
    try:
        plaintext = get_template('emailsadd/email.txt')
        htmly = get_template('emailsadd/user_reminder.html')
        d = Context({'participant_name': participant_name_reminder,
                     'participant_email_reminder': participant_email_reminder, 'event_name': event_name})
        subject, from_email, to = event_name, 'donotreplypitaya@gmail.com', participant_email_reminder
        print("subject " + subject + " from_email " + from_email + " to " + to)
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        # settings.STATIC_ROOT + "pic_folder/" + new_activity.pic
        image_file = open(event_pic.path, 'rb')
        msg_image = MIMEImage(image_file.read())
        image_file.close()
        msg_image.add_header('Content-ID', '<image1>')
        msg.mixed_subtype = 'related'
        msg.attach(msg_image)
        msg.send()
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


def send_email_survey(event_name, participant_name_survey, participant_email_survey, participant_id, event_id):
    try:
        plaintext = get_template('emailsadd/email.txt')
        htmly = get_template('emailsadd/invitesurvey.html')
        d = Context({'participant_id': str(participant_id)})
        subject, from_email, to = event_name, 'donotreplypitaya@gmail.com', participant_email_survey
        print("subject " + subject + " from_email " + from_email + " to " + to)
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.mixed_subtype = 'related'
        msg.send()
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


class Command(BaseCommand):
    help = 'Send mails according to current date'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        print("db.connections.databases " + db.connections.databases['default']['NAME'] + " db.engine " +
              db.connections.databases['default']['ENGINE'])
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        print(yesterday)
        print(tomorrow)
        today = datetime.date.today()

        # datetime.datetime.strptime(
        yesterday_events = Booker.objects.filter(
            date__gte=datetime.date(yesterday.year, yesterday.month, yesterday.day),
            date__lt=datetime.date(today.year, today.month, today.day))
        tomorrow_events = Booker.objects.filter(date__gt=datetime.date(today.year, today.month, today.day),
                                                date__lte=datetime.date(tomorrow.year, tomorrow.month, tomorrow.day))

        print(tomorrow_events)

        print("eventos de ontem yesterday_events.count() = " + str(yesterday_events.count()))
        for event in yesterday_events:
            event_date = event.date
            event_name = event.event_name
            participants = Newsletter.objects.filter(booker_id_id=event.id, approved=True)
            print("tomorrow_events participants.count() = " + str(participants.count()))
            for attender in participants:
                print('inside tomorrow_events participants')
                participant_name_survey = attender.participants_name
                participant_email_survey = attender.participants_email
                participant_id = attender.id
                event_id = attender.booker_id_id

                send_email_survey(event_name, participant_name_survey, participant_email_survey, participant_id,
                                  event_id)

        print("eventos de amanha tomorrow_events.count() = " + str(tomorrow_events.count()))
        for event in tomorrow_events:
            event_date = event.date
            event_pic = event.pic
            event_name = event.event_name
            participants = Newsletter.objects.filter(booker_id=event.id, approved=True)
            print("yesterday_events participants.count() = " + str(participants.count()))
            for attender in participants:
                print('inside yesterday_events participants')
                participant_name_reminder = attender.participants_name
                participant_email_reminder = attender.participants_email

                send_email_reminder(event_name, participant_email_reminder, participant_name_reminder, event_pic)





                # self.stdout.write('Successfully closed poll "%s"' % event.id)
