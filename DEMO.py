import os

# Ejemplo de vulnerabilidad: Inyección de comandos
def command_injection(user_input):
    os.system(user_input)  # Potencial de ejecutar comandos maliciosos

# Ejemplo de vulnerabilidad: XSS
def xss_example(user_input):
    print(f"<html><body>{user_input}</body></html>")  # No se filtra la entrada del usuario

# Ejemplo de vulnerabilidad: CSRF
import requests

def csrf_example(url, token, data):
    # No se valida el token, lo que permite ataques CSRF
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, data=data)
    return response

# Ejemplo de vulnerabilidad: SQL Injection
import sqlite3

def sql_injection_example(user_input):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE name='{user_input}'")  # Vulnerable a SQL Injection
    rows = c.fetchall()
    return rows

# Ejemplo de vulnerabilidad: Información sensible expuesta
def sensitive_information():
    api_key = "1234567890abcdef"  # Información sensible expuesta
    print(f"API Key: {api_key}")

if __name__ == "__main__":
    # Uso de las funciones con entrada no segura
    command_injection("ls")  # Solo para demostración, no usar en producción
    xss_example("<script>alert('XSS');</script>")
    csrf_example("http://example.com/api", "dummy_token", {"key": "value"})
    sql_injection_example("'; DROP TABLE users;--")
    sensitive_information()
