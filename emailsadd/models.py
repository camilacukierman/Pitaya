from django.db import models


class Booker(models.Model):
    manager_name = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    time = models.DateTimeField(null=True)
    date = models.DateTimeField(null=True)
    duration = models.DurationField(null=True)
    participants_number= models.IntegerField(null=True)
    participants = models.EmailField(max_length=254, blank=False, unique=True,
        error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'},)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return ' '.join([
            self.manager_name,
            self.event_name,
            self.location,
        ])







