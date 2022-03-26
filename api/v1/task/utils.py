import smtplib
from datetime import timedelta
from email.mime.text import MIMEText
from typing import List

from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
from rest_framework.generics import get_object_or_404

from task.models import Message


class SendMessageWithGmail:
    def __init__(self, data):
        self.host = settings.EMAIL_HOST
        self.port = settings.EMAIL_PORT
        self.sender = settings.EMAIL_HOST_USER
        self.sender_password = settings.EMAIL_HOST_PASSWORD
        self.recipient = data.get('email')
        self.data = data

    def send(self):
        try:
            self.validate()
            html = render_to_string(template_name='task/send_message_template.html', context=self.data)
            msg = MIMEText(html, "html")
            msg['Subject'] = self.data.get('subject')
            msg['From'] = self.sender
            msg['To'] = self.recipient

            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls()
                server.login(user=self.sender, password=self.sender_password)
                server.sendmail(self.sender, self.recipient, msg.as_string())
                server.quit()
            message = get_object_or_404(Message, id=self.data.get('id'))
            message.is_send = True
            message.save()
            return True
        except:
            return False

    def validate(self):
        if not self.sender and self.sender_password:
            raise ValueError("Логин и пароль отправителя не найдены")


def get_messages() -> List:
    now = timezone.now()
    now_plus_1 = now + timedelta(minutes=1)
    messages = Message.objects.filter(is_active=True, is_send=False,
                                      shipping_time__range=[now, now_plus_1]).values_list(
        'id', 'receiver__email', 'receiver__first_name', 'receiver__last_name', 'subject', 'content')
    result_list = []
    for message in messages:
        result_list.append(dict(zip(["id", "email", "first_name", "last_name", "subject", "content"], message)))
    return result_list
