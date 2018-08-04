from datetime import datetime
from gmail import GMail, Message
from random import choice

gmail = GMail ('Ngoc Anh <nabi.253@gmail.com>', 'Ngocanh123')

reasons = [ ''' <p style="text-align: center;">(Ốm) H&ocirc;m nay mặt mũi ti&ecirc;u điều</p>
<p style="text-align: center;">Ở nh&agrave; cho khỏe, kh&ocirc;ng liều được đ&acirc;u</p>''', 
'''<p style="text-align: center;">(T&igrave;m ch&oacute;) Ch&oacute; nh&agrave; em đ&atilde; biết y&ecirc;u</p>
<p style="text-align: center;">Đi đ&acirc;u mải miết, th&ocirc;i ti&ecirc;u mất rồi? :'(</p>
<p>&nbsp;</p>''']
reason = choice(reasons) 

html_content = """
<p style="text-align: center;"><span style="color: #ff0000;">ĐƠN XIN NGHỈ HỌC</span></p>
<p style="text-align: center;"><em><span style="color: #ff00ff;">Thanh xu&acirc;n tr&ocirc;i m&atilde;i chẳng về</span></em></p>
<p style="text-align: center;"><em><span style="color: #ff00ff;">Sao ta lầm lũi mải m&ecirc; học h&agrave;nh</span></em></p>
<p style="text-align: center;"><em><span style="color: #ff00ff;">Th&ocirc;i th&igrave; ta nghỉ nh&eacute; Anh</span></em></p>
<p style="text-align: center;"><em><span style="color: #ff00ff;">L&yacute; do l&agrave; thứ vừa nhanh vừa nhiều</span></em></p>
{{sickness}}
"""
 
html_to_send = html_content.replace("{{sickness}}", reason)

msg = Message ('Đơn xin nghỉ học', to = 'nabi.253@gmail.com', html = html_to_send )

while loop = True:
    now = datetime.now()
    if now.hour == 19:
        gmail.send(msg)
        break
      
   



