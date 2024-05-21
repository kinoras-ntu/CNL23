# Author: Miroslav Houdek <miroslav.houdek@gmail.com>
# License is, do whatever you wanna do with it (at least I think that that is what LGPL v3 says)

import smtpd
import asyncore
import smtplib
import traceback
from email.parser import Parser
from mailmsg import MailMessage


class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        mailfrom.replace("'", "")
        mailfrom.replace('"', "")

        for recipient in rcpttos:
            recipient.replace("'", "")
            recipient.replace('"', "")

        try:
            msg = Parser().parsestr(data.decode("utf-8"))
            msg.add_header("X-SPAM-STATUS", "YES")
            modified_data = msg.as_string().encode("utf-8")

            message = MailMessage(data)
            print(message.check())

            pass
        except:
            pass
            print("Something went south")
            print(traceback.format_exc())

        try:
            server = smtplib.SMTP("127.0.0.1", 10026)
            server.sendmail(mailfrom, rcpttos, modified_data)
            server.quit()
            print("Sent Successfully")
        except smtplib.SMTPException:
            print("Exception SMTPException")
            pass
        except smtplib.SMTPServerDisconnected:
            print("Exception SMTPServerDisconnected")
            pass
        except smtplib.SMTPResponseException:
            print("Exception SMTPResponseException")
            pass
        except smtplib.SMTPSenderRefused:
            print("Exception SMTPSenderRefused")
            pass
        except smtplib.SMTPRecipientsRefused:
            print("Exception SMTPRecipientsRefused")
            pass
        except smtplib.SMTPDataError:
            print("Exception SMTPDataError")
            pass
        except smtplib.SMTPConnectError:
            print("Exception SMTPConnectError")
            pass
        except smtplib.SMTPHeloError:
            print("Exception SMTPHeloError")
            pass
        except smtplib.SMTPAuthenticationError:
            print("Exception SMTPAuthenticationError")
            pass
        except:
            print("Undefined exception")
            print(traceback.format_exc())

        return


server = CustomSMTPServer(("127.0.0.1", 10025), None)

asyncore.loop()
