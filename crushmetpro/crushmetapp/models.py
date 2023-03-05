from django.db import models
from django.contrib.auth.models import User

GENDER = (('MALE','MALE'),
          ('FEMALE','FEMALE'),
         )

HOBBIES = (('SPORTS','SPORTS'),
           ('FITNESS','FITNESS',),
           ('MUSIC','MUSIC',),
           ('TRAVEL','TRAVEL'),
           ('READING','READING'),
           ('COOKING','COOKING'),
           ('ART & CULTURE','ART & CULTURE'),
           ('GAMING','GAMING'),
           ('FOOD & DRINK','FOOD & DRINK'),
           ('VOLUNTEER WORK','VOLUNTEER WORK')
          )

SHOWS = (('COMEDY','COMEDY'),
         ('DRAMA','DRAMA'),
         ('SCIENCE-FICTION','SCIENCE-FICTION'),
         ('FANTASY','FANTASY'),
         ('CRIME','CRIME')
        )

AGE_PREF = (('18-22','18-22'),
            ('23-27','23-27'),
            ('28-32','28-32'),
            ('33-40','33-40'),
            ('41+','41+'),
            )
class DemoProfile(models.Model):
     username=models.CharField(max_length=100,default="ABC")
     gender = models.CharField(max_length=50)
     gpref = models.CharField(max_length=50)
     interest=models.CharField(max_length=100,null=True)
     show=models.CharField(max_length=100,null=True)
     pickup=models.CharField(max_length=1000,null=True)
     about=models.CharField(max_length=2000,null=True)
     city=models.CharField(max_length=200,null=True)
     dob=models.DateField(blank=True,null=True)
     img=models.ImageField(blank=True,null=True)

     @property
     def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True,null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=50,choices=GENDER)
    hobby = models.CharField(max_length=50,choices=HOBBIES)
    favshows = models.CharField(max_length=50,choices=SHOWS)
    gpref = models.CharField(max_length=50,choices=GENDER)
    agepref = models.CharField(max_length=50,choices=AGE_PREF)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 

    def __str__(self):
        return self.name
    