SUBJECT = 'Доступ в АСУЗД'
TO = 'to'
FROM = 'asuzd@rosseti-ural.ru'
text = 'Приветствую!' + '\n'

BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
    ))
print(BODY)
