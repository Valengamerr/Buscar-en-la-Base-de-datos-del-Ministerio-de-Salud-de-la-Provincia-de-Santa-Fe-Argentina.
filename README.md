# 🔍 Buscador Padrón de Salud - Santa Fe

Este script de Python permite automatizar consultas al sistema del **Padrón de Salud de la Provincia de Santa Fe**. Está diseñado para imitar una petición de navegador y extraer información sobre coberturas médicas de forma rápida.

---

## 🚀 Guía de Instalación y Uso

### 🪟 En Windows

> [!IMPORTANT]
> **Paso 1: Instalación de Python**
> Descargá Python desde la **Microsoft Store** (buscá "Python 3.12"). Es la forma más fácil para que los comandos funcionen de una en tu terminal.

1. **Descarga el script:** Guarda tu archivo como `buscador_arg.py`.
2. **Abrí la Terminal:** Presioná la tecla `Windows`, escribí `cmd` y dale a Enter.
3. **Instalá la librería necesaria:** Copiá y pegá este comando en la terminal:
   ```bash
   pip install requests

En Linux (Ubuntu / Debian / Mint)
[!TIP] En Linux, Python ya suele venir instalado, pero es necesario instalar el gestor de paquetes y la librería de forma manual para que el script funcione.

Abrí una Terminal: Podés usar el atajo Ctrl + Alt + T.

Instalá los requerimientos: Copiá y pegá el siguiente comando:

Bash
sudo apt update && sudo apt install python3-pip python3-requests -y
Ubicá el archivo: Entrá a la carpeta donde descargaste el script.

Ejemplo: cd ~/Descargas

Ejecutá el script:

Bash
python3 buscador_arg.py
🛠️ Configuración de Datos (IMPORTANTE)
[!WARNING] ¡Atención! El código NO funcionará si no editás los datos de búsqueda. Abrí el archivo buscador_arg.py con un editor de texto y completá estos campos en la sección payload:
