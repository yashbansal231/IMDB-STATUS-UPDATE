from getData import getContentInf as inf
import pandas as pd
from sendMail import send_mail as sm
import re

global data

def isValidEmail(email):
 if len(email) > 7:
    if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) is not None:
        return True
 return False


def getId(name):
    try:
        return str(data[data['Name']==name.lower()]['Id'].values[0])
    except:
        return "No Match"
email = input("Enter Email Id : ").strip()
while(True):
    if isValidEmail(email) is True:
        break
    else:
        print("Invalid Email Address Try Again")
        email = input("Enter Email Id : ").strip()
names = list(input("Enter the series name(seperated by \',\') : ").split(','))
email_text = ""
data = pd.read_csv('data/moreids.csv')
for name in names:
    g_id = getId(name.strip())
    if getId(name.strip()) is not "No Match":
        email_text += "Name = " + name + "\nStatus = " + inf(g_id) + "\n\n"
    else:
        print(g_id)
try:
    sm(email_text,email)
    print("Mail Sent")
except:
    print("Mail Not Sent")