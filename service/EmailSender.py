import smtplib
import logging as log
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class EmailSender:
    def __init__(self, debug, server, port, from_mail, from_password, recipients, subject):
        self.debug = debug
        self.server = server
        self.port = port
        self.from_mail = from_mail
        self.from_password = from_password
        self.recipients = recipients
        self.subject = subject

    def send(self, content, image=None):
        if not self.debug:
            data = self.__create_email_data()
            if image is not None:
                data.attach(MIMEText(content))
                image_data = self.__create_image_data(image)
                data.attach(image_data)
            session = self.__login()
            session.sendmail(self.from_mail, self.recipients, data.as_string())
            session.quit()
        log.info("Sent email with content: " + content)

    def __create_image_data(self, image):
        image_data = MIMEImage(open(image, 'rb').read(), 'jpg')
        image_data.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
        return image_data

    def __login(self):
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo()
        session.login(self.from_mail, self.from_password)
        return session

    def __create_email_data(self):
        email_data = MIMEMultipart()
        email_data['Subject'] = self.subject
        email_data['To'] = self.recipients
        email_data['From'] = self.from_mail
        return email_data
