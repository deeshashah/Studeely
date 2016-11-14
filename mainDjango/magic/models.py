from django.db import models

class ListOfTopic(models.Model):
    topicName = models.CharField(max_length=50)
    topicUrl = models.URLField(max_length=100)
    topicSlug = models.CharField(max_length=50)