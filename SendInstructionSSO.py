import os
import smtplib
import sys
from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate


# ----------------------------------------------------------------------
def send_email_with_attachment(subject, body_text, to_emails, cc_emails, file_to_attach, file_name_to_attach):
    """
    Send an email with an attachment
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")
    header = 'Content-Disposition', 'attachment; filename="%s"' % file_name_to_attach

    # get the config
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    # extract server and from_addr from config
    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")

    # create the message
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)

    if body_text:
        msg.attach(MIMEText(body_text))

    msg["To"] = ', '.join(to_emails)
    msg["cc"] = ', '.join(cc_emails)

    attachment = MIMEBase('application', "octet-stream")

    try:
        with open(file_to_attach, "rb") as fh:
            data = fh.read()

        attachment.set_payload(data)
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg = "Error opening attachment file %s" % file_to_attach
        print(msg)
        sys.exit(1)

    emails = to_emails + cc_emails
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, emails, msg.as_string())
    server.quit()


if __name__ == "__main__":
    # emails = ["abduragimov.ga@gmail.com"]
    cc_emails = ["g.a.s.a.n66@mail.ru"]

    subject = "Упрощенный вход в АСУЗД!"
    body_text = "Приветствуем!" + '\n' +\
                "Уважаемые пользователи АСУЗД, спешим обрадовать вас тем, что теперь АСУЗД поддерживает" \
                " единую аутентификацию." + '\n' +\
                "Больше нет необходимости запоминать/сохранять в браузере/хранить в почте пароль " \
                "от АСУЗД. Можно просто воспользоваться кнопкой \"Войти через SSO\" и вы в системе!" + '\n' +\
                "Подробная инструкция находится во вложении к этому письму."
    file_name = 'InstructionForSSO.pdf'
    path = 'C:\\Users\\abduragimov-ga\\PycharmProjects\\Mail\\InstructionForSSO.pdf'

    # send_email_with_attachment(subject, body_text, emails, cc_emails, path, file_name)
    i = 1
    with open('Emails_new', 'r') as emails:
        for email in emails:
            print(i, email.split(sep=None))
            send_email_with_attachment(subject, body_text, email.split(sep=None), cc_emails, path, file_name)
            i += 1
