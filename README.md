
#  Portafolio Web Personal

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Deploy](https://img.shields.io/badge/Deploy-PythonAnywhere-yellow.svg)](https://gabidev1.pythonanywhere.com/)

> 🔗 **[Visita la demo en vivo aquí](https://gabidev1.pythonanywhere.com/)**

## 📖 Resumen Ejecutivo

**Portafolio Web** es una plantilla ligera pensada para presentar proyectos y habilidades de forma clara y profesional. Está diseñada para ser fácil de desplegar, personalizar y mantener; ideal para desarrolladores que buscan una presencia online rápida y robusta.

---

##  Características Principales

* **Diseño Responsivo:** Interfaz limpia, enfocada en el contenido y adaptable a cualquier tamaño de pantalla.
* **Estructura Modular:** Separación clara entre la lógica de negocio (`src/`), las vistas (`templates/`) y los recursos (`static/`).
* **CSS Minimalista:** Estilos ligeros, fáciles de leer y de sobreescribir.

---

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu sistema:
* [Python 3.8 o superior](https://www.python.org/downloads/)
* Gestor de paquetes `pip`

---

##  Instalación y Ejecución Local

Sigue estos pasos para levantar el proyecto en tu entorno de desarrollo:

1. **Obtén el proyecto:** Descarga y descomprime el paquete ZIP (o clona este repositorio en tu carpeta de trabajo).

2. **Crea un entorno virtual:**
```bash
python -m venv venv
```

3. **Activa el entorno virtual:**
   * *En Mac/Linux:*
```bash
source venv/bin/activate
```
* *En Windows:*
```bash
venv\Scripts\activate   
 ```

4. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta la aplicación:**
   ```bash
   python src/main.py
   ```
   *Una vez encendido el servidor, abre tu navegador web en la dirección local indicada por la consola (generalmente `http://127.0.0.1:5000/`).*

---

## 📂 Estructura del Proyecto

```text
📦 portafolio-web
 ┣ 📂 src/             # Código fuente y punto de entrada (main.py)
 ┣ 📂 templates/       # Plantillas HTML (Vistas)
 ┣ 📂 static/          # CSS, imágenes y recursos estáticos
 ┗ 📜 requirements.txt # Lista de dependencias para el despliegue
```

---

## 🎨 Personalización Rápida

* **Textos y Secciones:** Modifica los archivos HTML dentro de la carpeta `templates/` para actualizar tu información personal, experiencia y proyectos.
* **Estilos Visuales:** Edita el archivo `static/style.css` para adaptar los colores, márgenes y tipografías a tu propia marca personal.

```
