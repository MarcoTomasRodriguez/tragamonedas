from typing import List
import smtplib, ssl
from getpass import getpass
from dataclasses import dataclass
from datetime import date
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


@dataclass
class Receiver:
    first_name: str
    last_name: str
    email: str

receivers: List[str] = [Receiver(first_name="Alejo", last_name="Scarlato", email="a.alejo.scarlato@schonthal.esc.edu.ar")]

port = 465  # SSL Port
email = input("Ingrese su email: ")
password = getpass("Ingrese su contraseña: ")

# Create a secure SSL context
context = ssl.create_default_context()

def generate_report(receiver: Receiver) -> MIMEMultipart:
    report = MIMEMultipart()
    report['Subject'] = 'Reporte Estadístico - Tragamonedas'
    report['From'] = email
    report['To'] = receiver.email

    report.attach(MIMEText(f"""\
Estimado {receiver.last_name} {receiver.first_name},

A continuación, se le envía un reporte el cual contiene un cuadro estadístico, realizado automáticamente luego de la participación de cada usuario dentro del juego, \
en este caso se puede comprobar el porcentaje del total de tiros que devolvieron un determinado valor, entre 1 y 6.

Atentamente,
Rodríguez Marco y Scarlato Alejo

Fecha de Emisión: {date.today().strftime("%d/%m/%Y")}
"""
    ))

    pdf = MIMEApplication(open("report.pdf", "rb").read())
    pdf.add_header("Content-Disposition", "attachment", filename="Reporte.pdf")
    report.attach(pdf)

    return report


with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)

    for receiver in receivers:
        server.sendmail(email, receiver.email, generate_report(receiver).as_string())