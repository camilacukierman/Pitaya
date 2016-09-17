import datetime
from django.core.management.base import BaseCommand, CommandError

from emailsadd.models import Booker
def send_email(new_mail, new_activity, template):
    try:
        plaintext = get_template('emailsadd/email.txt')
        htmly = get_template(template)
        d = Context({'booking': new_activity, "invitee": new_mail})
        subject, from_email, to = new_activity.event_name, 'pitayaproject@gmail.com', new_mail.participants_email
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
        print("eventos de ayer")
        for event in yesterday_events:
            print(event.date)
            print(event.event_name)


        print("eventos de manaan")

        for event in tomorrow_events:
            print(event.date)
            print(event.event_name)

    # self.stdout.write('Successfully closed poll "%s"' % event.id)


