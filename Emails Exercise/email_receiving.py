import email
import imaplib

M = imaplib.IMAP4_SSL("imap.gmail.com")

email_str = input("Email: ")
password = input("Password: ")

M.login(email_str, password)

print(M.list())
print(M.select("inbox"))

typ, data = M.search(None, 'SUBJECT "Special email for testing"')

print(typ)
print(data)

email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')
print(email_data)
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')


email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
