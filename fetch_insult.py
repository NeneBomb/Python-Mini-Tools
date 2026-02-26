#!/usr/bin/env python3
"""
fetch_insult.py
Desc: Consulta la API de evilinsult, extrae el insulto (grep-style) y lo imprime.
Uso: python3 fetch_insult.py
"""

import sys
import json
import re

URL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

# función fetch que usa requests si está disponible, si no urllib
def fetch(url, timeout=6):
    try:
        import requests
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except Exception:
        # fallback a urllib si requests no está o falló
        try:
            from urllib import request as _request
            with _request.urlopen(url, timeout=timeout) as r:
                b = r.read()
            return b.decode('utf-8', errors='replace')
        except Exception as e:
            raise RuntimeError(f"Error al recuperar URL: {e}")

def extract_insult(raw_text):
    """
    Grep-like: busca primero con regex el par "insult":"...".
    Si no encuentra, intenta parsear JSON.
    Devuelve el insulto como string o None si no se encontró.
    """
    # regex simple para encontrar "insult": "..."
    m = re.search(r'"insult"\s*:\s*"([^"]+)"', raw_text)
    if m:
        return m.group(1)
    # intentar parsear JSON más robusto
    try:
        data = json.loads(raw_text)
        if isinstance(data, dict) and "insult" in data:
            return data["insult"]
    except Exception:
        pass
    return None

def main():
    try:
        raw = fetch(URL)
    except Exception as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)

    insult = extract_insult(raw)
    if not insult:
        print("No se encontró el insulto en la respuesta.", file=sys.stderr)
        print("Respuesta completa (para debug):\n", raw, file=sys.stderr)
        sys.exit(2)

    # imprimir el insulto en terminal
    print(insult)

if __name__ == "__main__":
    main()
