from email.mime import text

from cv2 import *
from datetime import *
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders




gmail_user = "XXXXXX"
gmail_pwd = "XXXXXXX"
to = "XXXXXX"
subject = "Security Breach"
text = "There is some activity in your home. See the attached picture."


while True:
    # need to check here if camera is busy
    cam = cv2.VideoCapture(0)
    s, img = cam.read()
    cam = cv2.VideoCapture(0)
    print("Saving Photo")
    picname = datetime.now().strftime("%y-%m-%d-%H-%M")
    picname = picname + '.jpg'
    cv2.imwrite(picname, img)
    print("Sending email")
    attach = picname

    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()
    print("Email Sent")
    os.remove(picname)

    # if s:    # frame captured without any errors
    #   imshow("Meet", img)
    # imwrite("/Users/meetjethwa21/Desktop/Meet.jpg", img) #save image



