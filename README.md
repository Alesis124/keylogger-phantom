# Keylogger Builder – Proyecto Educativo

⚠️ **ADVERTENCIA IMPORTANTE**  
Este proyecto ha sido desarrollado **exclusivamente con fines educativos** y de investigación académica, para su ejecución en **laboratorios controlados** y **sistemas propios**.  
**No debe utilizarse** en equipos de terceros ni sin consentimiento explícito.

El autor no se hace responsable del uso indebido del software.

---

## 🎓 Objetivo del proyecto

- Comprender cómo funcionan los *hooks* de teclado en **Linux** y **Windows**.
- Analizar la captura de eventos del sistema (teclas, portapapeles y capturas de pantalla).
- Estudiar diferencias reales entre plataformas.
- Aprender el flujo de empaquetado con **PyInstaller**.
- Integrar servicios serverless (Cloudflare Workers) para recepción y almacenamiento de datos.
- Identificar problemas de compatibilidad entre sistemas (encoding, finales de línea, permisos, etc.).
- Darse cuenta de que muchos antivirus no avisan de verdaderos problemas.

Todo el enfoque es **formativo**, no ofensivo.

---

## 🧠 Arquitectura general

El proyecto se divide en dos bloques principales:

### 1) Builder (`build.py`)
Script interactivo que:
- Solicita configuración (plataforma, modo stealth, persistencia, screenshots, intervalos).
- Genera keyloggers reales para **Linux**, **Windows** o ambos.
- Inserta la configuración directamente en los scripts generados.
- Crea scripts `.bat` para compilar en Windows usando `python -m PyInstaller`.
- Genera guías y scripts de instalación.

### 2) Keyloggers generados
Cada keylogger:
- Captura **teclas reales** mediante `pynput`.
- Captura **portapapeles** (opcional).
- Captura **screenshots periódicos** (opcional).
- Envía datos de texto a un **webhook** (por ejemplo Discord).
- Envía capturas de pantalla y backups de texto a un **Cloudflare Worker**.

---

## ☁️ Envío de capturas con Cloudflare Workers

El proyecto incorpora el envío automático de **screenshots** cada X segundos a un **Cloudflare Worker**, el cual puede:

- Recibir imágenes por:
  - `multipart/form-data`
  - bytes directos (`image/png`)
  - JSON con Base64
- Almacenar imágenes en **Cloudflare R2**.
- Guardar metadatos como:
  - nombre de la máquina
  - timestamp
  - método de captura
- Actuar como **backup** cuando un webhook no está disponible.

Este enfoque evita depender de plataformas externas y permite un flujo **controlado y privado**.

---

## 📊 Servicios compatibles (ejemplo)

El sistema de envío está diseñado para ser flexible y compatible con distintos servicios webhook:

| Servicio           | Estilo webhook | Acepta archivos  | Almacenamiento | Gratis      |
| ------------------ | -------------- | ---------------- | -------------- | ----------- |
| Discord webhook    | Sí             | No               | No             | Sí          |
| Slack webhook      | Sí             | Sí (limitado)    | Básico         | Sí          |
| Teams webhook      | Sí             | Indirecto        | No             | Sí          |
| Webhook.site       | Sí             | Sí (transitorio) | Temporal       | Sí          |
| **Cloudflare Workers** | **Sí**     | **Sí**           | **Sí (R2)**    | **Gratis tier** |
| Supabase Functions | Sí             | Sí               | Sí             | Gratis tier |
| Firebase Functions | Sí             | Sí               | Sí             | Gratis tier |

> Recomendado para el proyecto: **Cloudflare Workers + R2**.

---

## ⚙️ Requisitos

### Requisitos generales
- Python **3.10+**
- pip actualizado

### Instalación básica
```bash
pip install -r requirements.txt
```

### Dependencias clave
- `pynput`
- `requests`
- `pyinstaller`
- `pyperclip`
- `mss` / `scrot` / `pyautogui`
- `pywin32` (Windows)

> Algunas dependencias son **específicas de Windows** y no se instalan desde Linux.

---

## 🪟 Compilación en Windows (IMPORTANTE)

Windows puede interpretar incorrectamente archivos `.bat` creados en Linux.

### Problema común
- Linux: finales de línea **LF**
- Windows: finales de línea **CRLF**

### Solución
Antes de ejecutar el `.bat`:

**Opción 1 – unix2dos**
```bash
unix2dos COMPILAR_*.bat
```

**Opción 2 – Editor**
- Abrir en VS Code o Notepad++
- Cambiar finales de línea a **CRLF**
- Guardar

---

## 🧪 Modo simulación

Si no se introduce un webhook:
- El sistema entra en **modo simulación**
- No se envían datos externos
- Ideal para prácticas y demostraciones académicas

---

## 📁 Archivos generados

- `linux_keylogger_fixed_int_*.py`
- `windows_keylogger_worker_*.py`
- `COMPILAR_FIXED_INT_*.bat`
- `install_linux_int_*.sh`
- `GUIA_INSTALACION_*.txt`
- `config_*.json`

---

## 🔐 Consideraciones éticas y legales

Este proyecto existe para:
- Formación en ciberseguridad
- Análisis del funcionamiento interno de sistemas
- Prácticas en entornos controlados

❌ **No usar para**:
- Espiar usuarios reales
- Robar información
- Ejecutar en equipos ajenos
- Vulnerar leyes de privacidad

El mal uso puede conllevar **responsabilidad legal**.

---

## 🧾 Licencia

Proyecto educativo sin licencia comercial.  
Uso restringido a fines académicos y de aprendizaje.

---

## ✍️ Nota final

Este README deja constancia explícita de:
- La finalidad educativa del proyecto
- El uso de Cloudflare Workers como backend
- Las limitaciones técnicas reales
- Las precauciones necesarias al trabajar entre Linux y Windows
