import smtplib

from email.message import EmailMessage

def main():
	user = '' 		# Your email goes here
	password = ''	# Your password goes here

	try:
		server = smtplib.SMTP(host='smtp.gmail.com', port=587)
		server.starttls()
		server.login(user, password)

		message = EmailMessage()

		message.set_content('Hello there\nThis is a python email test.')

		message['From'] = user
		message['To'] = ''	# The destination email goes here
		message['Subject'] = 'Python email from Pedro'

		server.send_message(message)

		server.quit()

	except:
		print('somiethin went wrong')

if __name__ == '__main__':
	main()