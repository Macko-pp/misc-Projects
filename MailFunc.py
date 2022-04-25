import smtplib
import fire
from dotenv import load_dotenv
import os

load_dotenv()
_EMAIL_ = os.getenv('EMAIL')
_PASSWORD_ = os.getenv('PASSWORD')

def MailFunc(to, subject):
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(_EMAIL_, _PASSWORD_)

		msg = f'Subject: {subject}\n\n{input("Enter your message: ")}'

	try:
		smtp.sendmail(_EMAIL_,
			to, msg)
	except:
		print("Not a valid email address")

if __name__ == '__main__':
	fire.Fire(MailFunc)
