import platform 
import sys
from colorama import init, Fore, Style

init()

print(Fore.GREEN + Style.BRIGHT + "\n--- INICIANDO DIAGNÓSTICO DE WSL ---")
print(Style.RESET_ALL)

sistema = platform.system()
print(f"Sistema Operativo detectado: {Fore.CYAN}{sistema}{Style.RESET_ALL}")

if sistema == "Linux":
    print(Fore.GREEN + " Correcto, Python está corriendo en el subsistema Linux")
else:
    print(Fore.RED + " Alerta Estás corriendo en Windows")

print(f"\nVersión de Pyhthon: {Fore.YELLOW}{sys.version.split()[0]}{Style.RESET_ALL}")

print(Fore.MAGENTA + "\nEstado de la misión: Exitoso, tu entorno está listo para trabajar.")
print(Style.RESET_ALL)