#!/bin/python3

# Script used to send e-mails of test results

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sys import argv
import logging


def send_mail(from_email, to_emails, subject, email_contents):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        plain_text_content=email_contents)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY').strip())
        response = sg.send(message)
        logging.info('email with test results sent to: {}'.format(to_emails))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    from_email = os.environ.get('FROM_EMAIL')
    to_emails_env = os.environ.get('TO_EMAILS')


    # for creating a iterable from comma seperated list
    to_emails = [email.strip() for email in to_emails_env.strip().split(',') if email.strip()]

    script, subject, email_contents = argv
    send_mail(from_email, to_emails, subject, email_contents, api_key)

