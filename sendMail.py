import smtplib

user_name = "yyashbansalyash@gmail.com" #"**UserName**"
password =  "9983111175" #"**Pass**"
def send_mail(content,email_id):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(user_name, password)
    s.sendmail("Hi@HI.com", email_id, content) 
    s.quit()


send_mail("Chutiye","yashbansal231@gmail.com")
