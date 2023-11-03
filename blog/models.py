from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime
import uuid, random
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta
from django.utils.timezone import now


# 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 git access token
# Create your models here.
class Html(models.Model):
    id = models.IntegerField(default=1, primary_key=True, editable=True, unique=True)
    title = models.CharField(max_length=300)
    body_one = models.TextField(null=True, blank=True)
    body_two = models.TextField(null=True, blank=True)
    body_three = models.TextField(null=True, blank=True)
    body_four = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    like_num = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Html"
    def __str__(self):
            return f"{self.title} for number {self.id}"
    def get_absolute_url(self):
        return reverse("all_html", args=[self.id])
   
class Random(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "Random"
    def __str__(self):
            return self.title

class Css(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "Css"
    def __str__(self):
            return self.title
   
class JavaScript(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "JavaScript"
    def __str__(self):
            return self.title
   
class BootStrap(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "BootStrap"
    def __str__(self):
            return self.title
   
class Python(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_si = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "Python"
    def __str__(self):
            return self.title
   
class Django(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "Django"
    def __str__(self):
            return self.title

class React(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "React"
    def __str__(self):
            return self.title

class Comments(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "comments"

class MySQL(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "MySQL"
    def __str__(self):
            return self.title

class ML(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "ML"
    def __str__(self):
            return self.title

class TypeScript(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.CharField(max_length=300)
    link_two = models.CharField(max_length=300)
    link_three = models.CharField(max_length=300)
    link_four = models.CharField(max_length=300)
    link_five = models.CharField(max_length=300)
    link_six = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "TypeScript"
    def __str__(self):
            return self.title
   
class Newsletter(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.subject

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    verification_code = models.CharField(max_length=30)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.email




















