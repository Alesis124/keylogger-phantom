# Keylogger Builder – Proyecto Educativo

⚠️ **ADVERTENCIA IMPORTANTE**  
Este proyecto ha sido desarrollado **exclusivamente con fines educativos** y de investigación académica, para su ejecución en **laboratorios controlados** y **sistemas propios**.  
**No debe utilizarse** en equipos de terceros ni sin consentimiento explícito.

El autor no se hace responsable del uso indebido del software.

---

## 🎓 Objetivo del proyecto

- Comprender cómo funcionan los *hooks* de teclado en **Linux** y **Windows**.
- Analizar la captura de eventos del sistema (teclas, portapapeles y screenshots).
- Estudiar diferencias reales entre plataformas.
- Aprender el flujo de empaquetado con **PyInstaller**.
- Identificar problemas de compatibilidad entre sistemas (encoding, finales de línea, permisos, etc.).

Todo el enfoque es **formativo**, no ofensivo.

---

## 🧠 Arquitectura general

El proyecto se divide en dos bloques:

### 1) Builder
Script interactivo que genera:
- Un keylogger para **Linux**.
- Un keylogger para **Windows**.
- Archivos `.bat` para compilar en Windows usando `python -m PyInstaller`.
- Guía de instalación y configuración.

### 2) Keyloggers generados
- **Linux**: captura teclado real mediante `pynput`, opcionalmente portapapeles y screenshots.
- **Windows**: captura teclado (pyHook / fallback a pynput), portapapeles (pywin32) y screenshots (pyautogui).
- Envío opcional de datos mediante webhook (modo simulación disponible).

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
- `pyperclip` (Linux clipboard)
- `Pillow` / `pyautogui` (screenshots)
- `pywin32` / `pyHook` (Windows)

> Nota: Algunas dependencias **solo se instalan en Windows** y no pueden instalarse desde Linux.

---

## 🪟 Compilación en Windows (IMPORTANTE)

Por motivos de **seguridad**, Windows puede bloquear o ejecutar incorrectamente archivos `.bat` creados en Linux.

### 🔴 Problema común
Si el archivo `.bat` se ha creado en Linux, Windows puede no interpretarlo correctamente debido al tipo de salto de línea.

- Linux usa: **LF**
- Windows usa: **CRLF**

### ✅ Solución
Antes de ejecutar el `.bat` en Windows:

**Opción 1 – Usar `dos2unix` / `unix2dos`**
```bash
unix2dos COMPILAR_*.bat
```

**Opción 2 – Editor de texto**
- Abrir el `.bat` en VS Code / Notepad++
- Cambiar el formato de finales de línea a **CRLF**
- Guardar el archivo

Esto es obligatorio para que el `.bat` funcione correctamente en Windows.

---

## 🧪 Modo simulación

Si no se introduce un webhook:
- El sistema funciona en **modo simulación**
- No se envían datos externos
- Ideal para pruebas locales y demostraciones académicas

---

## 📁 Archivos generados

- `linux_real_keylogger_*.py`
- `windows_keylogger_fixed_*.py`
- `COMPILAR_FIXED_*.bat`
- `COMPILAR_SIMPLE_*.bat`
- `GUIA_INSTALACION_*.txt`
- `config_*.json`

---

## 🔐 Consideraciones éticas y legales

Este proyecto existe para:
- Formación en ciberseguridad
- Aprendizaje de bajo nivel del sistema
- Pruebas en entornos propios

❌ **No usar para**:
- Espiar usuarios
- Robar información
- Ejecutar en equipos ajenos
- Saltarse leyes de privacidad

El mal uso puede conllevar **responsabilidad legal**.

---

## 🧾 Licencia

Proyecto educativo sin licencia comercial.  
Uso restringido a fines académicos y de aprendizaje.

---

## ✍️ Nota final

Este README existe para dejar constancia clara de:
- La intención educativa del proyecto
- Sus limitaciones técnicas reales
- Las precauciones necesarias al trabajar entre Linux y Windows
