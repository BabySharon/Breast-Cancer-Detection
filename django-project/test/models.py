from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
 
class Patient(models.Model):
    pname = models.CharField(max_length = 100)
    age = models.IntegerField()
    testfile = models.FileField(upload_to='images/', )
    date_uploaded = models.DateTimeField(default=timezone.now)
    doctor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #App to be used in a laboratory
    #Even if the doctor account deleted patient records are to be saved
    #If the patient record is to be deleted when doctor is deleted, then, add argument, on_delete=models.CASCADE
    #An autoincrementing integer field is automatically added by django

    def __str__(self):
        return self.pname


class userModel(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    institution = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} profile'
