import smtplib

from jinja2 import Environment, FileSystemLoader


def send_email(sender, sender_pwd, recipients_string, subject, body):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('email_base.html')
    email_text = template.render(email_from=sender, email_to=recipients_string, email_subject=subject, body=body)
    recipients_list = recipients_string.split(', ')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender, sender_pwd)
    server.sendmail(sender, recipients_list, email_text)
    server.close()
