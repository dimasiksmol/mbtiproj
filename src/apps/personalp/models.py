from datetime import datetime
from django.db import models
#from django.conf import settings
from django.contrib.auth.models import User
from django.conf.global_settings import LANGUAGES
#from django.db.models.signals import post_save
#from django.dispatch import receiver


# Create your models here.
class Personal_info(models.Model):
    user = models.ForeignKey(User, null = True, on_delete=models.CASCADE, related_name='personal_info')
    nick_name = models.CharField(max_length = 100, blank=True)
    description = models.TextField(max_length = 10000, blank=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, blank=True,null=True)
    location = models.CharField(max_length=30, blank=True)
    img_pers = models.ImageField(upload_to = 'avatar', blank=True)
    social_type = models.CharField(max_length = 30, blank=True)
    ip_address = models.GenericIPAddressField(unpack_ipv4=True, null=True, verbose_name='IP адрес', blank=True)
    last_activity = models.DateTimeField(verbose_name='Время последней активности', blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    language = models.CharField(max_length=7, choices=LANGUAGES, default='ru')
    created_at = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return str(self.pk) + ".) " + str(self.user.last_name) + " " + self.user.first_name + " " + self.nick_name
    def __str__(self):
        if self.user:
            return str(self.pk) + ".) " + str(self.user.last_name) + " " + self.user.first_name + " " + self.nick_name
        else:
            return str(self.pk)

        # автолинкование профиля пользователя к пользователю при его сохранении
    #def user_post_save(sender, instance, **kwargs):
    #    ( profile, new ) = Personal_info.objects.get_or_create(user=instance)

    #models.signals.post_save.connect(user_post_save, sender=User)
    #class Personal_infoManager(models.Model):
    #    def create_person(self):
    #        new_person = self.create()

    # first_name = models.CharField(max_length = 30)
    # last_name = models.CharField(max_length = 50)
    # email_pers = models.EmailField(default="@mail.ru")

    #@receiver(post_save, sender=User)
    #def create_user_profile(sender, instance, created, **kwargs):
    #    if created:
    #        Personal_info.objects.create(user=instance)

    #@receiver(post_save, sender=User)
    #def save_user_profile(sender, instance, **kwargs):
    #    instance.personal_info.save()

