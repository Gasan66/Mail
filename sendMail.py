import smtplib
import pyodbc

HOST = "mail.rosseti-ural.ru"
SUBJECT = "Test email from Python"
TO = "abduragimov.ga@gmail.com"
FROM = "python@mydomain.com"
text = "Python 3.4 rules them all!"

BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
))

server = smtplib.SMTP(HOST)
server.sendmail(FROM, TO, BODY)
server.quit()