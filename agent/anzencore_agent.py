import os
import platform
import subprocess
import requests
import json
from datetime import datetime

class AnzenCoreAgent:
    def __init__(self):
        # Configuración de conexión (Usa los mismos datos de tu proyecto)
        self.supabase_url = "https://hnwradnsykylksjvrmpb.supabase.co"
        self.supabase_key = "sb_publishable_Sh4c3OF_PXYUnZcUAF6uTQ_qI3Oga8T" # La encuentras en Project Settings > API
        self.usuario_id = None # Se pedirá al iniciar

    def obtener_info_dispositivo(self):
        print("📱 Identificando hardware...")
        # Detectar si es Tablet o Smartphone por la resolución o modelo (Simulado para Python)
        modelo = platform.machine()
        os_ver = f"{platform.system()} {platform.release()}"
        
        # Lógica de identificación
        tipo = "Smartphone"
        if "pad" in modelo.lower() or "tablet" in modelo.lower():
            tipo = "Tablet"
            
        return {
            "nombre": f"{platform.node()} ({modelo})",
            "tipo": tipo,
            "os": os_ver
        }

    def escanear_vulnerabilidades(self):
        print("🔍 Escaneando aplicativos y sistema...")
        hallazgos = []

        # 1. Chequeo de Root (Vulnerabilidad de Sistema)
        if os.path.exists("/system/app/Superuser.apk") or os.path.exists("/sbin/su"):
            hallazgos.append({
                "cat": "Sistema", "app": None, "tit": "Acceso Root Detectado",
                "desc": "El dispositivo está rooteado, rompiendo el sandbox de seguridad.",
                "niv": "Crítico"
            })

        # 2. Escaneo de Aplicativos (Simulación de apps instaladas)
        # En Android real con Termux usarías: subprocess.check_output(["pm", "list", "packages"])
        apps_a_verificar = [
            {"nombre": "WhatsApp", "package": "com.whatsapp", "status": "Seguro"},
            {"nombre": "Flashlight Free", "package": "com.evil.spyware", "status": "Malicioso"},
            {"nombre": "Unknown App", "package": "com.proxy.handler", "status": "Sospechoso"}
        ]

        for app in apps_a_verificar:
            if app["status"] != "Seguro":
                hallazgos.append({
                    "cat": "Aplicativo",
                    "app": app["nombre"],
                    "tit": f"App {app['status']} detectada",
                    "desc": f"El paquete {app['package']} presenta comportamiento inusual.",
                    "niv": "Alto" if app["status"] == "Malicioso" else "Medio"
                })

        return hallazgos

    def enviar_a_cloud(self, info_disp, hallazgos):
        print(f"📤 Enviando {len(hallazgos)} hallazgos a AnzenCore Cloud...")
        
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json"
        }

        # 1. Registrar/Obtener ID del dispositivo
        disp_data = {
            "usuario_id": self.usuario_id,
            "nombre_modelo": info_disp["nombre"],
            "tipo": info_disp["tipo"],
            "os_version": info_disp["os"]
        }
        r_disp = requests.post(f"{self.supabase_url}/rest/v1/dispositivos", 
                               json=disp_data, headers=headers)
        
        # 2. Crear cabecera de escaneo
        escaneo_data = {
            "usuario_id": self.usuario_id,
            "riesgo_global": "Alto" if len(hallazgos) > 0 else "Bajo",
            "total_vulnerabilidades": len(hallazgos)
        }
        r_esc = requests.post(f"{self.supabase_url}/rest/v1/escaneos", 
                              json=escaneo_data, headers=headers)

        print("✅ Auditoría finalizada. Revisa tu Dashboard de AnzenCore.")

    def iniciar(self):
        print("--- ANZENCORE LOCAL AGENT v1.0 ---")
        self.usuario_id = input("Ingrese su ID de Usuario (Lo verá en su perfil web): ")
        
        info = self.obtener_info_dispositivo()
        fallos = self.escanear_vulnerabilidades()
        self.enviar_a_cloud(info, fallos)

if __name__ == "__main__":
    agent = AnzenCoreAgent()
    agent.iniciar()