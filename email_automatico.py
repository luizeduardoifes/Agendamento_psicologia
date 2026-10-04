from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

def enviar_email(nome_cliente, email_cliente, data, hora, servico):
    email_remetente = os.getenv("EMAIL_REMETENTE")
    senha_email = os.getenv("SENHA_EMAIL")
    data_formatada = data.strftime("%d/%m/%Y")

    if not email_remetente or not senha_email:
        raise ValueError("As variáveis de ambiente EMAIL_REMETENTE e SENHA_EMAIL não estão definidas.")

    mensagem = MIMEMultipart()
    mensagem['From'] = email_remetente
    mensagem['To'] = email_cliente
    mensagem["Reply-To"] = email_remetente
    mensagem['Subject'] = "Seu agendamento foi realizado com sucesso!"

    corpo_email = f"""
    Olá, {nome_cliente}!
    Seu agendamento está confirmado!!!
    Data: {data_formatada}
    Hora: {hora}
    Serviço: {servico}
    local: Rua das Flores, 123 - Centro, Cidade XYZ
    favor comparecer com 15 minutos de antecedência.
    obrigado por escolher nossos serviços!
    """

    mensagem.attach(MIMEText(corpo_email, 'plain'))

    servidor = None

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.ehlo()
        servidor.starttls()
        servidor.ehlo()
        servidor.login(email_remetente,senha_email)

        servidor.send_message(mensagem)
        print("funcionou")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}") 
