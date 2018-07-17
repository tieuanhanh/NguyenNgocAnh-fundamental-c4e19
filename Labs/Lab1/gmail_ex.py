from gmail import GMail, Message
from random import choice

gmail = GMail ('Ngoc Anh <nabi.253@gmail.com>', 'Ngocanh123')

reasons = ["mình bị ốm", "mình ngủ quên", "mình về quê với bố mẹ", "mình đi chơi"]
reason = choice(reasons)

html_content = """
<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p>&nbsp;</p>
<p style="text-align: center;"><span style="color: #ff0000;"><strong>ĐƠN XIN NGHỈ HỌC</strong></span></p>
<p>&nbsp; &nbsp; &nbsp; K&iacute;nh gửi: Thầy gi&aacute;o cute lớp C4E 19 Tuấn Anh</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Trợ giảng Qu&acirc;n Ngố</p>
<p>&nbsp; &nbsp; &nbsp; M&igrave;nh l&agrave; Ngọc Anh, học vi&ecirc;n của lớp C4E 19. H&ocirc;m nay m&igrave;nh nghỉ nh&eacute; do {{sickness}}</p>
<p>&nbsp; &nbsp; &nbsp; M&igrave;nh sẽ l&agrave;m b&agrave;i tập đầy đủ.&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp;</p>
"""
html_to_send = html_content.replace ("{{sickness}}", reason)


msg = Message ('Đơn xin nghỉ học', to = 'nabi.253@gmail.com', html = html_to_send)
gmail.send(msg)
