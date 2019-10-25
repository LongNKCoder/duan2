from django.db import models
from django.core.cache import cache 
import datetime
from chotot import settings
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11,unique=True, blank=False)
    state = models.BooleanField(default = False)
    balance = models.IntegerField(default = 0)
    pic = models.ImageField(upload_to='pic', blank=False, default="pic/default.jpg")
    
    def __str__(self):
        return self.user.username
    
    def last_seen(self):
        return cache.get('seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                        seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False 