import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid
from dotenv import dotenv_values

config = dotenv_values(".env")


# noinspection PyStringFormat
class SendEmail:

    def __init__(self):
        self.email = "andrewkyle@andrewkyle.dev"
        self.password = config.get("EMAIL_PASSWORD")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_email_message(self, sender_data):

        if sender_data["phone"] != "":
            phone_num = [digit for digit in sender_data["phone"]]
            phone = f"({phone_num[0]}{phone_num[1]}{phone_num[2]}) {phone_num[3]}{phone_num[4]}{phone_num[5]}" \
                            f"-{phone_num[6]}{phone_num[7]}{phone_num[8]}{phone_num[9]}"
        else:
            phone = "No phone number provided"
        if sender_data['name'] == "":
            subject = f"New email from Personal Site"
        else:
            subject = f"New email from Personal Site sent by {sender_data['name']}"

        # Message Container
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = Address(sender_data["name"], addr_spec=sender_data["email"])
        msg['To'] = Address(display_name="Andrew Kyle",
                            addr_spec="andrewkyle@andrewkyle.dev")
        msg.add_alternative(f"""
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                {sender_data["message"]}
                <br>
                <p>Sender Phone Number: {phone}</p>
                <p>Sender Email: {sender_data["email"]}</p>
            </body>
        </html>
        """, subtype='html')

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            connection.send_message(msg=msg)

        print("Email sent successfully")

    def send_reset_conf(self, user_data, conf_code):
        # Message Container
        msg = EmailMessage()
        msg['Subject'] = "Password Reset Confirmation Code"
        msg['From'] = Address("Do Not Reply", addr_spec="contact@andrewkyle.dev")
        msg['To'] = Address(display_name=user_data["name"],
                            addr_spec=user_data["email"])
        msg.add_alternative(f"""
                <!DOCTYPE html>
                <html>
                    <head></head>
                    <body>
                        <p>Hello {user_data["name"]},</p>
                        <br>
                        <p>This email was sent because a password reset was requested. Your confirmation number is: {conf_code}<p> 
                        <br>
                        <p>If you did not submit this request, then just ignore this email.<p>
                        <br>
                        <p>Take care,<br>Andrew's Blog<p>
                    </body>
                </html>
                """, subtype='html')

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            connection.send_message(msg=msg)