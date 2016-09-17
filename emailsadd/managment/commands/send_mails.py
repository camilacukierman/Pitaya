from django.core.management.base import BaseCommand, CommandError

from emailsadd.models import Booker


class Command(BaseCommand):
    help = 'Send mails according to current date'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):


            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
