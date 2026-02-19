import smtplib
import os
from dotenv import load_dotenv

smptp = smtplib.SMTP("smtp.gmail.com", 587)
smptp.starttls()
load_dotenv()
smptp.login('sasportsvid@gmail.com',os.getenv("SMTP_PASS"))
print('Login Succesful!')
smptp.quit()