from django.db import models


class Booker(models.Model):
    manager_name = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50)
    event_description = models.CharField(max_length=1000, null=True)
    location = models.CharField(max_length=50)
    to_time = models.TimeField()
    from_time = models.TimeField()
    date = models.DateField()
    manager_message = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return ' '.join([
            self.manager_name,
            self.event_name,
            self.location,
        ])


class Newsletter(models.Model):
    booker_id = models.ForeignKey('Booker')
    participants_name = models.CharField(max_length=50, null=True)
    participants_email = models.EmailField(max_length=254, blank=False, unique=True,
                                           error_messages={'required': 'Please provide the email address.',
                                                           'unique': 'An account with this email exist.'}, )
