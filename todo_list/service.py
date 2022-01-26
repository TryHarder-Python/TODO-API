from django.core.mail import send_mail


def send_task(task_title, *args):
    message = 'This Task for you'
    send_mail(
        subject=task_title,
        message=message,
        from_email='task_service@myapp.com',
        recipient_list=[*args],
    )