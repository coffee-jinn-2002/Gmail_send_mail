import csv
from email.mime.text import MIMEText
import re
import smtplib
from email.header import Header
from time import sleep

def create_message(text, lst):
    res = text
    for i in range(1, len(lst)):
        res = re.sub('<<' + str(i) + '>>', lst[i], res)
    return res

# データベース部分は削除されました。

# 差出人名
send_name = 'YOUR_SEND_NAME'
charset = 'iso-2022-jp'

account = "YOUR_EMAIL_ADDRESS"
password = "YOUR_PASSWORD"

subject = "YOUR_EMAIL_SUBJECT"

csv_path = "path/to/your/sample.csv"
text_path = "path/to/your/sample.txt"

from_email = account

num = 0

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(account, password)
print(csv_path)
print("server login pass") 

with open(csv_path) as c:
    reader = csv.reader(c)
    send_list = [row for row in reader]
    print("csv_path pass")

with open(text_path) as t:
    text = t.read()
    print("text open pass")

for s in send_list:
    num += 1
    to_email = s[0]
    message = create_message(text, s)
    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg['From'] = '%s <%s>'%(Header(send_name.encode(charset), charset).encode(), account)
    try:
        server.send_message(msg)
        print("send email "+ str(num))
    except:
        print("sending NG: " + to_email)
    sleep(0.9)
    
server.quit()
print("All pass")
