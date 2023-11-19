from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import *
from .documents import *


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"

class LogQuerySerializer(DocumentSerializer):
    class Meta:
        document=LogsDocument
        fields=("level","message","resourceId","spanId","traceId","commit","metadata","timestamp")
       