from api.celery import celery_app
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from api.config.fastmail import conf
import asyncio


fm = FastMail(conf)


@celery_app.task(name='send_registration_email')
def send_email(subject: str, user_email: str, message_body: str):
    """Kullanıcı kayıt e-postası gönderir."""
    try:

        message = MessageSchema(
            subject=subject,
            recipients=[user_email],
            body=message_body,
            subtype="html",
        )

        asyncio.run(fm.send_message(message))
        print(f"E-posta başarıyla gönderildi: {user_email}")
        
    except Exception as e:
        print(f"E-posta gönderiminde hata oluştu: {str(e)}")


@celery_app.task(name='send-comments-author')
def send_comments(subject: str, user_email: str, message_body: str):
    """ Gönderiye yeni yorum eklenirse yazara mail gönderir. """

    comment_message = MessageSchema(
        subject=subject,
        recipients=[user_email],
        body=message_body,
        subtype="html",
    )

    try:
        asyncio.run(fm.send_message(comment_message))
        print(f"E-posta başarıyla gönderildi: {user_email}")
    except Exception as e:
        print(f"E-posta gönderiminde hata oluştu: {str(e)}")
