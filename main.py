#%%
import numpy as np
import smtplib
import random
import time

#%%
names = ['Marieke', 'Parisa', 'Gian', 'Wout']
emails = ['mariekevanbrussel@msn.com', 'mariekevanbrussel@msn.com', 'mariekevanbrussel@msn.com', 'mariekevanbrussel@msn.com']

emails_dict = dict(zip(names,emails))

draws = ['name'] * len(names)
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

print(draws_dict)

# %%
sender_email = "mariekevanbrussel@outlook.com"
password = input(str("Please enter your password: "))

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender_email, password)
print('Login Succes')

for name in names:
    rec_email = emails_dict[name]
    drawn = draws_dict[name]
    subject = f"Sinterklaas Lootjes Fissa in de Hissa"
    body = f"Hellowwww {name}, \n\n De geluksvogel voor wie jij een zeerkortetermijnsurprise en gedicht mag verzorgen is..... *drumrollss* \n\n {drawn} "
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail(sender_email, rec_email, message)
    print('Email has been sent to ', rec_email)
    time.sleep(5)




