from fastapi_mail import ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME"),
    MAIL_PORT=os.getenv("MAIL_PORT", 587),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=os.getenv("MAIL_STARTTLS", True),
    MAIL_SSL_TLS=os.getenv("MAIL_SSL_TLS", False),
)
