import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_object.ehlo())
print(smtp_object.starttls())

email = input("Email: ")
password = input("Password please: ")
smtp_object.login(email, password)

from_email = email
to_email = input("Email to send a message: ")

subject = input("Enter the subject line:")
message = input("Enter the message:")
msg = "Subject: " + subject + "\n" + message

smtp_object.sendmail(from_email, to_email, msg)
smtp_object.quit()