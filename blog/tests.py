from django.test import TestCase

# Create your tests here.
import smtplib

def test_smtp_server(host, port):
    try:
        server = smtplib.SMTP(host, port)
        server.quit()
        print("SMTP server is accessible.")
    except Exception as e:
        print(f"SMTP server is not accessible. Error: {e}")

# Usage
test_smtp_server('smtp.elasticemail.com', 2525)
# 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