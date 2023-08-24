import yagmail

# Email
email = 'alex27dz@gmail.com'
subject = 'test1'
body = 'hello world'
pass_auth = 'yeqnnbfgkfetetcr'

def send_email(email, subject, body):
    ya_email = yagmail.SMTP('alex27dz@gmail.com', pass_auth)
    ya_email.send(email, subject, body)
    print('email sent')


send_email(email, subject, body)
