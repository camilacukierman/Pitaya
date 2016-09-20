from django.contrib.auth.models import User
from django.db import models


class Booker(models.Model):
    user_id = models.ForeignKey(User, default=1)
    manager_name = models.CharField(max_length=50, null=True)
    event_name = models.CharField(max_length=50)
    event_description = models.CharField(max_length=1000, null=True)
    location = models.CharField(max_length=50)
    to_time = models.DateTimeField()
    from_time = models.DateTimeField()
    date = models.DateTimeField()
    manager_message = models.CharField(max_length=1000, null=True)
    pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img.jpg')

    def __str__(self):
        return ' '.join([
            self.manager_name,
            self.event_name,
            self.location,
        ])


class Newsletter(models.Model):
    booker_id = models.ForeignKey(Booker)
    participants_name = models.CharField(max_length=50, null=True)
    participants_email = models.EmailField(max_length=254, blank=False,
                                           error_messages={'required': 'Please provide the email address.',
                                                           'unique': 'An account with this email exist.'}, )
    approved = models.BooleanField(default=False)
    answer_survey = models.BooleanField(default=False)


class Survey(models.Model):
    participant_ref = models.ForeignKey(Newsletter, on_delete=models.CASCADE, default=1)
    booker_id = models.IntegerField(default=0)
    a1 = models.IntegerField(default=0)


