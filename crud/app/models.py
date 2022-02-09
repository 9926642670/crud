from django.db import models

# Create your models here.
class Persondetail(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    mob_no = models.IntegerField()
    choice_gender = [
        ('M', 'Male'), 
        ('F', 'Female'), 
        ('A', 'Another')
        ]
    gender = models.CharField(max_length=1, choices=choice_gender, default = "M")
    images = models.ImageField(upload_to = "media_fol")

    def __str__(self):
        return self.name