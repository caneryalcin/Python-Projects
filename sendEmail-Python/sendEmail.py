import smtplib #SMTP is required to connect to the mail server and to send an e-mail.

server = smtplib.SMTP('smtp.gmail.com', 587) #Connect a mail server and send it(587 is a port).
server.starttls()

server.login("username","password")
server.sendmail("sender@gmail.com","receiver@gmail.com","Your message")

server.quit()
