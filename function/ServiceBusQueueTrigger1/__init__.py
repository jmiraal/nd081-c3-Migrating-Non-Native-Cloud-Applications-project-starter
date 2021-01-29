import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    # TODO: Get connection to database
    # Update connection string information
    host = "postgresql-server-jmiraal.postgres.database.azure.com"
    dbname = "techconfdb"
    user = "jmiraal@postgresql-server-jmiraal"
    password = "Vendetta41!"
    sslmode = "require"

    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")

    try:
        # TODO: Get notification message and subject from database using the notification_id

        # TODO: Get attendees email and name

        # TODO: Loop through each attendee and send an email with a personalized subject

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        print("The Function has executed correctly")

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        # TODO: Close connection
        print("Sentence finally")