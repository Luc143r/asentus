from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Latest_product(models.Model):

    title = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    content = models.TextField(default="No description")
    background = models.ImageField(upload_to="static\\img\\970x647", default='01.jpg')
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Subscription(models.Model):

    ICONS = (
        ('service-icon icon-chemistry', 'Chimestry'),
        ('service-icon icon-badge', 'Badge'),
        ('icon-shield', 'Shield')
    )

    title = models.CharField(max_length=40)
    price = models.IntegerField()
    content = models.TextField(default="No description")
    options1 = models.CharField(max_length=40, default="Basic Features")
    options2 = models.CharField(max_length=40, default="Basic Features")
    options3 = models.CharField(max_length=40, default="Basic Features")
    published_date = models.DateTimeField(default=timezone.now)
    icon = models.CharField(max_length=40, choices=ICONS, default='service-icon icon-chemistry')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class About_us(models.Model):

    ICONS = (
        ('service-icon icon-chemistry', 'Chimestry'),
        ('service-icon icon-screen-tablet', 'Tablet'),
        ('service-icon icon-badge', 'Badge'),
        ('service-icon icon-notebook', 'Notebook'),
        ('service-icon icon-speedometer', 'Speedometer'),
    )

    title = models.CharField(max_length=40)
    content = models.TextField(default="No description")
    published_date = models.DateTimeField(default=timezone.now)
    icon = models.CharField(max_length=40, choices=ICONS, default='service-icon icon-chemistry')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Team(models.Model):

    name = models.CharField(max_length=40)
    vacancy = models.CharField(max_length=40)
    content = models.TextField(default="No description")
    background = models.ImageField(upload_to="static\\img\\770x860", default="01.jpg")
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Contact(models.Model):

    city = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    content = models.TextField(default="No description")
    number = models.CharField(max_length=40)
    mail = models.EmailField(max_length=254, blank=True, unique=True)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.city


class Feedback(models.Model):

    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, blank=False, unique=False)
    phone = models.CharField(max_length=40)
    message = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email
