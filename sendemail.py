import smtplib
import imghdr
from email.message import EmailMessage

def pcx_email(email_id):
    n=0

    while n<2:
        msg = EmailMessage()
        msg['Subject'] =  'NEED INSURANCE'
        msg['From'] = #email address to be sent from
        msg['To'] = {email_id}
        msg.set_content('My car broke down. My house is on fire. Check attached documents')

        #with open('car_accident.jpg', 'rb') as f:
            #file_data=f.read()
            #file_type = imghdr.what(f.name)
            #file_name=f.name

        #msg.add_attachment(file_data, maintype = 'image', subtype=file_type, filename=file_name)
        files = ['insurance.pdf', 'Insurance_Complaint.pdf']
        for file in files:
            with open(file, 'rb') as f:
                file_data=f.read()
                file_name=f.name

            msg.add_attachment(file_data, maintype = 'application', subtype='octet-stream', filename=file_name)



        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(#insert your email, insert your password )


            smtp.send_message(msg)

            n = n+1
            print(f"This is the value of n: {n}")




email_lists= [#list of emails to send]
p=0
while p<5:
    for email_list in email_lists:
        pcx_email(email_list)
        p=p+1
        print(f"This is the value of p: {p}")
