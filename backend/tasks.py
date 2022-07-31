import os
import requests
import pytz
import datetime
# from dotenv import load_dotenv
from requests import Response
from rest_framework import status

from backend.models import Message, Client, Newsletter



# load_dotenv()
URL = "https://probe.fbrq.cloud/v1/send/"
TOKEN = "***"


def send_sms(data, client_id, url=URL, token=TOKEN):
    client = Client.objects.get(pk=client_id)
    timezone = pytz.timezone(client.timezone)
    # now = datetime.datetime.now(timezone)

    # if mail.time_start <= now.time() <= mail.time_end:
    header = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'}
    print(URL + str(data['id']))
    response = requests.post(url=url + str(data['id']), headers=header, json=data)
    print(1)
    return 1
    # except requests.exceptions.RequestException as exc:
    #     print(exc)
    #     raise self.retry(exc=exc)
    # else:
    #     logger.info(f"Message id: {data['id']}, Sending status: 'Sent'")
    #     Message.objects.filter(pk=data['id']).update(sending_status='Sent')

    # time = 24 - (int(now.time().strftime('%H:%M:%S')[:2]) -
    #              int(mail.time_start.strftime('%H:%M:%S')[:2]))
    # logger.info(f"Message id: {data['id']}, "
    #             f"The current time is not for sending the message,"
    #             f"restarting task after {60 * 60 * time} seconds")
    # return self.retry(countdown=60)