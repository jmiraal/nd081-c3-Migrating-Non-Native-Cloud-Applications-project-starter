import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="postgresql-server-jmiraal.postgres.database.azure.com"
    POSTGRES_USER="jmiraal@postgresql-server-jmiraal"
    POSTGRES_PW=os.environ['POSTGRES_PW']
    POSTGRES_DB="techconfdb"
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY=os.environ['SECRET_KEY']
    SERVICE_BUS_CONNECTION_STRING =os.environ['SERVICE_BUS_CONNECTION_STRING']
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'jesus.mira1@hotmail.com'
    SENDGRID_API_KEY = ''#Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False