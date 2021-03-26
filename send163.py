import sys,os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sendfile(f,path='upload'):
    print(f)
    message=MIMEMultipart()
    message['From'] = '<safeei@126.com>'
    message['Subject'] = Header(f, 'utf8').encode()
    message['To'] = '<safeei@126.com>'
    attr2 = MIMEText(f, 'plain', 'utf-8')
    message.attach(attr2)
    attr1=MIMEText(open('/'+path+'/'+f,'rb').read(),'base64','utf-8')
    attr1["content_Type"]='application/octet-stream'
    attr1["Content-Disposition"] = 'attachment; filename="'+f+'"' 
    message.attach(attr1)
    server = smtplib.SMTP('smtp.126.com', 25)
    server.login('safeei@126.com', 'GKCFSQMQYBSMRRRE')
    server.sendmail('safeei@126.com', ['safeei@126.com'],message.as_string())
    print(f+'ok')
os.system('split -b 50m '+sys.argv[1]+' _safeei')
path='upload'
if len(sys.argv)>2:
    path=sys.argv[2]
for f in os.listdir('/'+path+'/'):
    if f.startswith('_safeei'):
        sendfile(f,path)
