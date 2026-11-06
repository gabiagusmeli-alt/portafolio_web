# Portafolio de Gabriel Meli

Portafolio personal desarrollado con Flask, Jinja, HTML, CSS y JavaScript. Presenta proyectos personales y académicos de backend, aplicaciones de escritorio, C, sistemas y redes en una página adaptable a escritorio y móvil.

Demo: [gabidev1.pythonanywhere.com](https://gabidev1.pythonanywhere.com/)

## Ejecutar localmente


```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

En Windows, activá el entorno con `venv\Scripts\activate`.

La aplicación requiere credenciales SMTP para enviar el formulario de contacto. Configurá estas variables en `src/.env`:

```env
MAIL=tu-cuenta@gmail.com
PASSWORD=tu-clave-de-aplicacion
MAIL_DESTINO=destino@correo.com
```



Iniciá el servidor desde la raíz del proyecto:

```bash
python src/main.py
```

Luego abrí `http://127.0.0.1:5000/`.

## Estructura

```text
src/
├── main.py
├── static/
│   ├── foto.png
│   └── style.css
└── templates/
    └── index.html
```

Los proyectos y datos personales se editan en `src/templates/index.html`; los estilos adaptables están en `src/static/style.css`.

La selección incluye enlaces a los repositorios originales. Los trabajos académicos se identifican como proyectos en equipo; consultá cada README para conocer el alcance y las pruebas de cada uno.
