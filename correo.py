import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def enviar_correo_con_imagen(from_address, to_address, subject, body_text, numEntrenamientos, smtp_server, smtp_port, password):
    # Asignación del archivo PDF según el número de días de entrenamiento
    pdf_path = "./tablasEntrenoBase/entreno3dias.pdf" if numEntrenamientos == 3 else (
        "./tablasEntrenoBase/entreno4dias.pdf" if numEntrenamientos == 4 else "./tablasEntrenoBase/entreno5dias.pdf"
    )

    # Crear el objeto MIMEMultipart
    msg = MIMEMultipart('mixed')
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Crear la parte de texto/HTML del cuerpo
    cuerpo_html = f"""
    <html>
        <body>
            <p>{body_text}</p>
        </body>
    </html>
    """
    msg.attach(MIMEText(cuerpo_html, 'html'))

    # Incluir el archivo PDF como adjunto
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
            pdf_attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(pdf_path))
            msg.attach(pdf_attachment)
    except FileNotFoundError:
        print("El archivo PDF no se pudo encontrar.")
        return
    except Exception as e:
        print(f"Se produjo un error al adjuntar el archivo: {e}")
        return

    # Configurar el servidor SMTP
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_address, password)
        server.send_message(msg)
        server.quit()
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Se produjo un error al enviar el correo: {e}")



# Ejemplo de uso
numEntrenamientos = int(input("Introduce el número de días que va a entrenar -> "))
enviar_correo_con_imagen(
    from_address="ejemplo@ejemplo.com",
    to_address=input("Introduce el correo electrónico -> "),
    subject="¡Tu plan de entrenamiento personalizado está listo!",
    body_text=f'''<p>Estimado/a Cliente/a,</p>
                  <p>Espero que estés bien. Me complace informarte que he preparado tu tabla de entrenamiento adaptada a tus necesidades y objetivos específicos.</p>
                  <p>Este plan está diseñado para maximizar tus resultados de forma efectiva y segura, teniendo en cuenta tu nivel actual de condición física y tus metas personales. En el documento adjunto, encontrarás una descripción detallada de cada ejercicio, junto con recomendaciones y consejos para sacar el máximo provecho de cada sesión.</p>
                  <p>Recuerda que el éxito de tu entrenamiento depende de tu dedicación y constancia. Estoy aquí para apoyarte en cada paso del camino, así que no dudes en ponerte en contacto si tienes preguntas o necesitas orientación adicional.</p>
                  <p>¡Comencemos este emocionante camino hacia una mejor versión de ti mismo/a!</p>
                  <p>¡Adelante y a entrenar!</p>
                  <p>Un saludo, <b>EJEMPLO</b>.</p>''',
    numEntrenamientos=numEntrenamientos,
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    password='Password'  # Usa una variable de entorno para mayor seguridad
)