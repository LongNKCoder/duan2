from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

class Brand(models.Model):
    name = models.CharField(max_length=255)

TYPE_CHOICES = (
    ('mua','Mua'),
    ('ban', 'Bán')
)
STATE_CHOICES = (
    ('open','Mở'),
    ('close','Đóng')
)

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    create_date = models.DateTimeField(default = now, editable = False)
    update_date = models.DateTimeField(default = now)
    price = models.IntegerField()
    state = models.CharField(max_length=6, choices=STATE_CHOICES, default='open')
    type_post = models.CharField(max_length=6, choices=TYPE_CHOICES, default='ban')
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name='post')
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE, related_name='images')
    pic = models.ImageField(upload_to='post/pic', blank=False)