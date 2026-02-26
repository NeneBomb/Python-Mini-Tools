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
