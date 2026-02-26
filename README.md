# 🐍 Python Mini-Tools Collection

Una colección de scripts pequeños y utilidades en Python que demuestran diferentes conceptos de programación, desde consumo de APIs hasta manipulación de archivos.

---

## 🌩️ Fetch-Insult
Un script que consulta la API de `evilinsult.com` para obtener un insulto aleatorio.

### ✨ Características / Features:
- **Resilience:** Sistema de fallback que usa `requests` o `urllib` según disponibilidad.
- **Data Extraction:** Extracción de datos mediante Expresiones Regulares (Regex) y parsing de JSON.
- **Error Handling:** Gestión de errores de red y de formato de respuesta.

### 🚀 Uso / Usage:
```bash
python3 fetch_insult.py

## 🔫 Revolver Roulette
Un juego de azar con lógica de turnos y arte ASCII. Demuestra el manejo de bucles y la librería `random`.

## 🌦️ Weather API
Script que consume la API de Open-Meteo para obtener el clima actual en Jerez. Ejemplo de manejo de peticiones `HTTP` y `JSON`.

## ⌨️ Simple Keylogger (PoC)
Un registrador de pulsaciones de teclas avanzado que utiliza codificación en **Base64** para el almacenamiento de logs.

### 🛡️ Notas de Indetectabilidad:
> **Nota técnica:** Este script ha sido diseñado manteniendo una estructura simple. En ciberseguridad ofensiva, minimizar las líneas de código y el uso de dependencias externas es crucial para evitar firmas heurísticas de los antivirus. La simplicidad reduce la "huella" (footprint) del malware en el sistema.

### ✨ Características:
- **Base64 Encoding:** Los logs no se guardan en texto claro, dificultando su análisis inmediato.
- **Clean Exit:** Utiliza la librería `atexit` para asegurar que el log se cierre correctamente.
- **Low Profile:** Ejecución ligera con consumo mínimo de recursos.

---

## ⚠️ Disclaimer Global / Legal Notice
Este repositorio contiene pruebas de concepto con fines exclusivamente educativos y de auditoría de seguridad ética. El uso de estos scripts en sistemas sin autorización expresa es ilegal. El autor no se responsabiliza del uso indebido de este material.

This repository contains proof-of-concept scripts for educational and ethical security auditing purposes only. Unauthorized use is illegal.
