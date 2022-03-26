from api.v1.task.utils import get_messages, SendMessageWithGmail
from conf.celery import app


@app.task(bind=True)
def send_message(self):
    print('[+] Starting send message')
    try:
        messages = get_messages()
        result_list = []
        if messages:
            for message in messages:
                gmail_server = SendMessageWithGmail(message)
                result = gmail_server.send()
                result_list.append(result)
            if all(result_list):
                return "[+] {0} messages successfully send!".format(len(messages))
            else:
                return "[-] An error has occurred"
        else:
            return "[-] Message not found!"
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
