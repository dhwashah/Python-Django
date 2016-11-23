from django.db import models

Network_choices = (
    ('airtel', 'Airtel'),
    ('vodafone', 'Vodafone'),
    ('docomo', 'Docomo'),
    ('idea', 'Idea'),
)

class Clients(models.Model):
    #auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    mob_no = models.BigIntegerField()
    network = models.CharField(max_length=20, choices = Network_choices, default='new')
    date = models.DateTimeField('date created', auto_now_add = True)
    dob =  models.DateField()

    def __str__(self):
        return self.name
