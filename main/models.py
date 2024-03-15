from django.db import models

# Home qismi
# subtitleni birinchi qo'yganimni sababi web sahifada birinchida turgandi
class Home(models.Model):
    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.FileField(upload_to='aboutus/')


class Service(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    service_title = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

