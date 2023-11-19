from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
   FilteringFilterBackend,
   CompoundSearchFilterBackend,
   SuggesterFilterBackend)
from logingest.serializers import *
from logingest.models import  Log
from logingest.documents import *
from elasticsearch_dsl import Q


class LogQueryView(DocumentViewSet):
   document=LogsDocument
   serializer_class = LogQuerySerializer

   filter_backends=[FilteringFilterBackend,CompoundSearchFilterBackend,SuggesterFilterBackend]
   search_fields=("level","message","resourceId","spanId","traceId","commit","metadata","timestamp")
   multi_match_search_fields=search_fields
   
   filter_fields={
      "level":"level",
      "message":"message",
      "resourceId":"resourceId",
      "spanId":"spanId",
      "traceId":"traceId",
      "commit":"commit",
      "metadata":"metadata",
      "timestamp":"timestamp",
   }
   
   def filter_queryset(self, queryset):
      search_params = self.request.query_params.get("search", "").split(",")

      q_objects = []
      for param_value in search_params:
         for param in param_value.split(","):
            key, value = param.split(":")
            if key in self.search_fields:
               if key == "timestamp":
                  q_objects.append(Q("range", **{key: {"gte": value,"lte": value}}))
               else:
                  q_objects.append(Q("match", **{key: {"query": value, "fuzziness": "auto"}}))
            elif param in self.filter_fields:
               queryset = queryset.filter(Q("term", **{self.filter_fields[key]: value}))
            elif key in self.multi_match_fields:
               queryset = queryset.filter(Q("multi_match", query=value, fields=self.multi_match_fields))

      if q_objects:
            query = Q("bool", must=q_objects)
            return queryset.query(query)

