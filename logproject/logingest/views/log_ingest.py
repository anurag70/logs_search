from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from logingest.serializers import *
from logingest.models import  Log


class LogIngestView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":f'log successfully saved for log_id {serializer.data.get("resourceId")}',"status":"success"}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)