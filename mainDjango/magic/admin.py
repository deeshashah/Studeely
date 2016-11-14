from django.contrib import admin
from magic.models import ListOfTopic

class ListOfTopicClass(admin.ModelAdmin):
      list_display    = ['topicName','topicUrl']

admin.site.register(ListOfTopic, ListOfTopicClass)
