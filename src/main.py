from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv
import os
import logging
import re
import socket
import time

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv()

# Validar que las variables de entorno existan
MAIL = os.getenv('MAIL')
PASSWORD = os.getenv('PASSWORD')
DESTINO = os.getenv('MAIL_DESTINO')

if not all([MAIL, PASSWORD, DESTINO]):
    logger.error("Faltan variables de entorno: MAIL, PASSWORD o MAIL_DESTINO")
    raise ValueError("No están configuradas las credenciales de email")

# Inicializar app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def pagina_principal():
    mensaje_error = None
    mensaje_exito = None

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
        mensaje = request.form.get('mensaje', '').strip()

        # Validaciones
        if not nombre or not email or not mensaje:
            mensaje_error = "Todos los campos son obligatorios"
            logger.warning("Intento de envío con campos vacíos")

        elif not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            mensaje_error = "El formato del correo es inválido"
            logger.warning(f"Intento con email inválido: {email}")

        elif len(mensaje) > 5000:
            mensaje_error = "El mensaje es demasiado largo (máximo 5000 caracteres)"
            logger.warning(f"Mensaje demasiado largo: {len(mensaje)} caracteres")

        else:
            # Intentar enviar el correo con reintentos
            max_retries = 3
            base_backoff = 1  # segundos

            for attempt in range(1, max_retries + 1):
                try:
                    logger.info(f"Intento de envío {attempt}/{max_retries}")
                    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
                        connection.starttls()
                        connection.login(user=MAIL, password=PASSWORD)

                        asunto = "Mensaje enviado desde la pagina del portafolio"
                        cuerpo = f"Tienes un mensaje de: {nombre} mail:{email} que dice:\n{mensaje}"
                        mensaje_formateado = f"Subject: {asunto}\n\n{cuerpo}".encode('utf-8')

                        connection.sendmail(from_addr=MAIL, to_addrs=DESTINO, msg=mensaje_formateado)

                    mensaje_exito = "¡Mensaje enviado correctamente! Nos pondremos en contacto pronto."
                    logger.info(f"Email enviado exitosamente desde: {email}")
                    break

                except smtplib.SMTPAuthenticationError:
                    mensaje_error = "Error de autenticación del servidor de correo. Contacta al administrador."
                    logger.error("Error de autenticación SMTP - credenciales inválidas")
                    break

                except smtplib.SMTPRecipientsRefused:
                    mensaje_error = "Error al procesar la dirección de destino. Contacta al administrador."
                    logger.error("Email de destino rechazado por el servidor SMTP")
                    break

                except smtplib.SMTPDataError:
                    mensaje_error = "El servidor rechazó el contenido del correo. Intenta nuevamente."
                    logger.error("Error en los datos del email - servidor rechazó el contenido")
                    break

                except (socket.gaierror, socket.timeout, ConnectionRefusedError, ConnectionError, TimeoutError, OSError, smtplib.SMTPConnectError) as e:
                    # Errores transitorios: reintentar
                    if attempt < max_retries:
                        wait = base_backoff * (2 ** (attempt - 1))
                        logger.warning(f"Error transitorio al enviar correo (intento {attempt}/{max_retries}): {e}. Reintentando en {wait}s")
                        time.sleep(wait)
                        continue
                    else:
                        # último intento falló
                        if isinstance(e, socket.gaierror):
                            mensaje_error = "No se puede resolver el servidor de correo. Verifica tu conexión a internet."
                            logger.error("Error de red: No se pudo resolver DNS para smtp.gmail.com")
                        elif isinstance(e, socket.timeout) or isinstance(e, TimeoutError):
                            mensaje_error = "La conexión al servidor se tardó demasiado. Intenta nuevamente."
                            logger.error("Error de red: Timeout al conectarse al servidor SMTP")
                        elif isinstance(e, ConnectionRefusedError):
                            mensaje_error = "El servidor de correo rechazó la conexión. Intenta más tarde."
                            logger.error("Error de red: Conexión rechazada por el servidor SMTP")
                        else:
                            mensaje_error = "No hay conexión con el servidor. Verifica tu internet."
                            logger.error(f"Error de red final: {str(e)}")
                        break

                except smtplib.SMTPException as e:
                    mensaje_error = "Ocurrió un error al enviar el correo. Intenta nuevamente."
                    logger.error(f"Error SMTP general: {str(e)}")
                    break

                except Exception as e:
                    mensaje_error = "Ocurrió un error inesperado. Intenta nuevamente más tarde."
                    logger.error(f"Error inesperado: {str(e)}")
                    break

    return render_template("index.html", mensaje_error=mensaje_error, mensaje_exito=mensaje_exito)


if __name__ == '__main__':
    app.run()
