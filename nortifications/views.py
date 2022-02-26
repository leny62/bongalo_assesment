from .serializers import NotifSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .helpers import send_email, send_sms
# Create your views here.

@swagger_auto_schema(method='post', request_body=NotifSerializer)
@api_view(['POST'])
def send_nortification(request):
    notif = NotifSerializer(data=request.data)
    
    if notif.is_valid():
        data = notif.validated_data
        
        if(data['type'] == 'email'):
            #send email here
            send_email(data['sender'], data['receiver'], data['msg'])
            notif.save()
            return Response(notif.data, status = status.HTTP_201_CREATED)

        elif(data['type'] == 'sms'):
            #send sms here
            send_sms(data['receiver'],data['msg'])
            notif.save()
            return Response(notif.data, status = status.HTTP_201_CREATED)

        elif(data['type'] == 'push'):
            #send push here
            notif.save()
            return Response(notif.data, status = status.HTTP_201_CREATED)

        else:
            return Response("The notification type is incorrect", status=status.HTTP_400_BAD_REQUEST)
    
    return Response(notif.errors, status=status.HTTP_400_BAD_REQUEST)