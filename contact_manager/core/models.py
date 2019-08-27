from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    how_did_you_first_meet = models.TextField()
    when_did_you_first_meet = models.DateField()

    def __str__(self):
        return self.name


class LastContactTalk(models.Model):
    last_contact_date = models.DateField()
    subject = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_contact_date}'

