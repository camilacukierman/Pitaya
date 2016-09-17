import datetime
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand, CommandError
from django.template import Context
from django.template.loader import get_template
from email.mime.image import MIMEImage

from emailsadd.models import Booker, Newsletter


def send_email_reminder (event_name, participant_email_reminder, participant_name_reminder,event_pic):
    try:
        plaintext = get_template('emailsadd/email.txt')
        htmly = get_template('emailsadd/user_reminder.html')
        d = Context({'participant_name': participant_name_reminder})
        subject, from_email, to = event_name, 'pitayaproject@gmail.com', participant_email_reminder
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
        print (message)

def send_email_survey(event_name,participant_name_survey,participant_email_survey):
            try:
                plaintext = get_template('emailsadd/email.txt')
                htmly = get_template('emailsadd/send_survey.html')
                d = Context({'participant_name': participant_name_survey})
                subject, from_email, to = event_name, 'pitayaproject@gmail.com', participant_email_survey
                text_content = plaintext.render(d)
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg_image.add_header('Content-ID', '<image1>')
                msg.mixed_subtype = 'related'
                msg.attach(msg_image)
                msg.send()
            except Exception as ex:
                template = "An exception of type {0} occured. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print (message)

class Command(BaseCommand):
    help = 'Send mails according to current date'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        today = datetime.date.today()

        yesterday_events = Booker.objects.filter(date__gt=yesterday,date__lt=today)
        tomorrow_events = Booker.objects.filter(date__gt=today,date__lt=tomorrow)

        print("eventos de ontem")
        for event in yesterday_events:
            event_pic = event.pic
            print(event.date)
            event_name = event.event_name
            participants = Newsletter.objects.filter(booker_id=event.id,approved=True)
            for attender in participants:
                participant_name_reminder = attender.participants_name
                participant_email_reminder = attender.participants_email
                send_email_reminder (event_name, participant_email_reminder,participant_name_reminder,event_pic)


        print("eventos de amanha")
        for event in tomorrow_events:
            print(event.date)
            event_name = event.event_name
            participants = Newsletter.objects.filter(booker_id=event.id,approved=True)
            for attender in participants:
                print(attender.participants_name)
                print(attender.participants_email)
                print(event.event_name)
                participant_name_survey = attender.participants_name
                participant_email_survey = attender.participants_email
                send_email_survey(event_name,participant_name_survey,participant_email_survey)




            # self.stdout.write('Successfully closed poll "%s"' % event.id)


