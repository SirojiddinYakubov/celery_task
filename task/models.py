from django.contrib.auth import get_user_model
from django.db import models
from tinymce.models import HTMLField

from common.models import BaseModel

User = get_user_model()


class Message(BaseModel):
    subject = models.CharField(max_length=255)
    content = HTMLField()
    shipping_time = models.DateTimeField()
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
