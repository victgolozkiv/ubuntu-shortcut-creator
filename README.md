# Ubuntu Shortcut Creator 🚀

Una herramienta sencilla y potente para automatizar la creación de accesos directos (`.desktop`) en Ubuntu. Olvídate de la terminal y de configurar permisos manualmente.

## ✨ Características

- **Interfaz Gráfica (GUI):** Crea lanzadores de forma visual y rápida.
- **Auto-Trust (GIO):** Olvida el molesto mensaje de "Allow Launching". La herramienta marca el acceso directo como confiable automáticamente.
- **Sin Terminal:** Los programas se ejecutan directamente en modo gráfico (sin ventanas negras de fondo).
- **Gestión de Rutas:** Soporta directorios de trabajo, iconos personalizados y comandos complejos.
- **Doble Registro:** Además del escritorio, registra la aplicación en el menú del sistema (`~/.local/share/applications`).

## 🛠️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/victgolozkiv/ubuntu-shortcut-creator.git
   cd ubuntu-shortcut-creator
   ```

2. Asegúrate de tener instalado Python 3 y Tkinter (normalmente viene por defecto en Ubuntu):
   ```bash
   sudo apt update
   sudo apt install python3-tk
   ```

## 🚀 Cómo usar

### 1. Interfaz Gráfica (Recomendado)
Ejecuta el creador visual:
```bash
python3 crear_lanzador_gui.py
```
Solo rellena los campos, selecciona tu icono y ¡listo! Tu acceso directo aparecerá en el escritorio.

### 2. Línea de Comandos (CLI)
Para los amantes de la terminal:
```bash
python3 crear_lanzador.py "Nombre" "Comando" "Ruta/Icono" "Directorio/Trabajo"
```

## 📂 Estructura del Proyecto

- `crear_lanzador_gui.py`: La aplicación principal con interfaz moderna (Tkinter).
- `crear_lanzador.py`: El motor que genera los archivos `.desktop` y gestiona los permisos de Ubuntu.

## 📝 Notas
- Al crear el primer acceso directo, si Ubuntu muestra una advertencia, dale a **"Trust and Launch"**. Gracias a la integración con `gio`, esto solo pasará una vez o ninguna.

---
Creado por [victgolozkiv](https://github.com/victgolozkiv)

## ❤️ Apoya el Proyecto

Si esta herramienta te ha sido útil, ¡considera invitarme a un café! Tu apoyo ayuda a seguir mejorando este y otros proyectos de código abierto.

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/paypalme/VictorRicardo162/1)

