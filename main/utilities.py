from django.template.loader import render_to_string
from django.core.signing import Signer
from online_board.settings import ALLOWED_HOSTS
from datetime import datetime
from os.path import splitext

signer = Signer


# Сигнал на отправку письма об успешнй регистрации
def send_activation_notification(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body_text = render_to_string('email/action_letter_body.txt', context)
    user.email_user =(subject, body_text)


# Созданеи названия медиа файлов
def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


# Сигнал на отправку письма об успешном добавлении комментария
def send_new_comment_notification(comment):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'

    author = comment.bb.author
    context = {'author': author, 'host': host, 'comment': comment}
    subject = render_to_string('email/new_comment_letter_subject.txt', context)
    body_text = render_to_string('email/new_comment_letter_body.txt', context)
    author.email_user =(subject, body_text)
