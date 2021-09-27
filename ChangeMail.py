import pyodbc
import smtplib
from email.header import Header
from email.mime.text import MIMEText

file = open('Query', 'r')
query = file.read()

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.80.52.11;DATABASE=ASUZD; Trusted_connection=yes')
if cnxn:
    print('Connect')


def changeMail(mailASUZD, mailAD):
    try:
        cursor.execute("""update AspNetUsers
                          set Email = ?,
                              UserName = ?
                          where Email = ?""", (mailAD, mailAD, mailASUZD))
    except pyodbc.DatabaseError as err:
        cnxn.rollback()
        return str(err)
    else:
        cnxn.commit()
        mail = 'Ok'
            # sendMail(mailAD)
        return mail


def sendMail(to):
    HOST = 'mail.rosseti-ural.ru'
    SUBJECT = 'Доступ в АСУЗД'
    TO = [to, 'abduragimov.ga@gmail.com', 'aamatveef@gmail.com']
    FROM = 'asuzd@rosseti-ural.ru'
    text = '\n'.join((
            'Приветствую!',
            'В рамках подключения АСУЗД к системе единой авторизации мы сменили ваш логин в системе АСУЗД. '
            'Вам необходимо выйти из системы и войти заново.',
            'Для входа в систему используйте логин: {}'.format(to),
            'Пароль остался прежним.',
            'Спасибо!'
    ))

    msg = MIMEText(text, 'plain', 'utf-8')
    msg['Subject'] = Header(SUBJECT, 'utf-8')
    msg['From'] = FROM
    msg['To'] = ','.join(TO)

    server = smtplib.SMTP(HOST)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    return text


cursor = cnxn.cursor()
rows = cursor.execute(query).fetchall()
print(len(rows))
for row in rows:
    log = changeMail(row.Email_ASUZD, row.Email_AD)
    cursor.execute('insert into _log_change_logins values (?, ?, ?, ?, ?)',
                   row.Email_ASUZD,
                   row.Email_AD,
                   log,
                   row.UsrAsuzdID,
                   row.UserName)
    cnxn.commit()
    print(row.Email_ASUZD, row.Email_AD, log)
    print(row)
cnxn.close()
