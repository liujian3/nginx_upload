mport sys,os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
u=sys.argv[2]
p='GDGRWRYVZBMEQPVO' if u=='safermd' else 'GKCFSQMQYBSMRRRE'
def sendfile(f):
    print(f)
    message=MIMEMultipart()
    message['From'] = '<'+u+'@126.com>'
    message['Subject'] = Header(f, 'utf8').encode()
    message['To'] = '<safeei@126.com>'
    attr2 = MIMEText(f, 'plain', 'utf-8')
    message.attach(attr2)
    attr1=MIMEText(open('./'+f,'rb').read(),'base64','utf-8')
    attr1["content_Type"]='application/octet-stream'
    attr1["Content-Disposition"] = 'attachment; filename="'+f+'"'
    message.attach(attr1)
    server = smtplib.SMTP('smtp.126.com', 25)
    server.login(u+'@126.com', p)
    server.sendmail(u+'@126.com', ['safeei@126.com'],message.as_string())
    print(f+'ok')
    os.remove('./'+f)
os.chdir('nginx_upload')
os.system('split -b 50m '+sys.argv[1]+' _'+sys.argv[1]+'_')
for f in os.listdir('.'):
    if f.startswith('_'+sys.argv[1]+'_'):
        sendfile(f)
