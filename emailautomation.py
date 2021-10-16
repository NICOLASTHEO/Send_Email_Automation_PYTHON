import os
import smtplib
from email.message import EmailMessage
from password import senha

# configurar email que enviará mensagem e senha
EMAIL_ADRESS = 'seuemail@provedor.com'
EMAIL_PASSWORD = senha

msg = EmailMessage()
msg['Subject'] = 'Automatizando envio de emails - Teste de Automação'
msg['From'] = 'seuemail@provedor.com'
msg['To'] = 'emailqvaireceber@gmail.com', 'outroemail@gmail.com', 'maisumemial@yahoo.com.br'

msg.set_content(
    'Automatizando envio de email com Python, sem precisar abrir o navegador. Vamos automatizar o Mundo!!! \n ESTUDE!!! \n Theo Nicolas QA')

# como enviar o emial:
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
