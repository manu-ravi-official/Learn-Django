from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='event_images/', default='event_images/default.jpg')

    def __str__(self):
        return f"Image for {self.event.name}"
