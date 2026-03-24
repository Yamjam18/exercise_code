import time
import os
import subprocess
from pynput import keyboard

running = True
contador = 1

# archivo donde se escribirá
archivo = os.path.expanduser("~/EstoyActivo.txt")

def on_press(key):
    global running
    if key == keyboard.Key.enter:
        print("ENTER presionado. Terminando...")
        running = False
        return False

# escuchar ENTER
listener = keyboard.Listener(on_press=on_press)
listener.start()

# crear archivo si no existe
open(archivo, "a").close()

# abrir Terminal mostrando el archivo en vivo
subprocess.Popen([
    "osascript",
    "-e",
    f'tell application "Terminal" to do script "tail -f {archivo}"'
])

print("Programa activo. Presiona ENTER para detener.")

while running:
    with open(archivo, "a") as f:
        f.write(f"Estoy activo #{contador}\n")

    contador += 1

    for _ in range(60):
        if not running:
            break
        time.sleep(1)

print("Programa finalizado")