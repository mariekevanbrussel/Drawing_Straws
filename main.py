#%%
import smtplib
import random
import time

"""
INPUT NEEDED
"""
names = ['Name1', 'Name2', 'Name3']
emails = ['email1@gmail.com', 'email2@gmail.com', 'email3@gmail.com']
sender_email = "senderemail@gmail.com"
host = 'smtp.office365.com'
port = 587
email_subject = "Drawing straws"
email_opening = "Hi "
email_body =  "You have drawn:"
email_closing = "Greetings from Sint and Piet"


"""
Start of code
"""

emails_dict = dict(zip(names,emails))
draws = [""] * len(names)
draws_dict = dict(zip(names, draws))
random.shuffle(names)

for name in names:
    if names.index(name) != (len(names)-1): #For all but the last one
        index_drawn = names.index(name) + 1
        drawn = names[index_drawn]
        draws_dict[name] = drawn
    else:
        drawn = names[0]
        draws_dict[name] = drawn

password = input(str("Please enter your password: "))
server = smtplib.SMTP(host, port)
server.starttls()
server.login(sender_email, password)
print('Login Succesfull')

for name in names:
    rec_email = emails_dict[name]
    drawn = draws_dict[name]
    message = f'Subject: {email_subject} \n\n {email_opening}{name} \n\n {email_body} {drawn} \n\n {email_closing} \n\n {closing_line}'
    server.sendmail(sender_email, rec_email, message)
    print('Email has been sent to ', rec_email)
    time.sleep(1)



    




