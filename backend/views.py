from rest_framework import viewsets, status

from backend.models import Client, Newsletter, Message
from backend.serializers import ClientSerializer, NewsletterSerializer, MessageSerializer
from rest_framework.response import Response

from backend.tasks import send_sms


class ClientViewset(viewsets.ModelViewSet):
    """Пользовательский Viewset"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageViewset(viewsets.ModelViewSet):
    """Viewset для сообщений"""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer



class NewsletterViewset(viewsets.ModelViewSet):
    """Viewset для рассылок"""

    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def create(self, request, *args, **kwargs):
        clients = Client.objects.all()
        text = request.data['message']
        for client in clients:
            data = {
                'id': '1',
                "phone": client.phone_number,
                "text": text
                }
            send_sms(data=data,client_id=client.id)
            return Response(data, status=status.HTTP_200_OK)


