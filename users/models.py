from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

''' using FileSystemStorage class in order to save profile pics into the specified folder which 
    in that case is the media root 
    media root folder path is set in settings.py file'''
fs = FileSystemStorage()

class Profile(models.Model):
    
    '''Custom profile class extends the user model for adding extra fields to user in a seperate 
       table that has one to one relationship with user table(user model) .
       User model is already provided by django'''
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(verbose_name="profile picture",storage=fs)
    undesired_words_count = models.IntegerField(default=0)  # the cumulative number of undesiredwords the user has used 
    is_locked = models.BooleanField(default=False) # determine whether the user is locked or not
    #categories   # there will be a relationship here many to many ( user -> categories)
    def __str__(self):
        return self.user.username

''' the following methods benifit from signals provided by django in order
    connect events between user model and profile model . for instance if a user is created
    a profile will be created automatically .. (magic)'''  
      
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
    
    
    
    

