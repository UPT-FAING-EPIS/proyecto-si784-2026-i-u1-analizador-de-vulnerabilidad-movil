import streamlit as st
import re
from src.models.scan_model import ScanModel
from src.services.ai_advisor import AIAdvisor
from src.domain.scanner_rules import ScannerRules

class ScanController:
    def __init__(self):
        self.model = ScanModel()
        self.ai = AIAdvisor()
        self.rules = ScannerRules()

    def obtener_ua(self):
        """Evita el AttributeError de st.context"""
        try:
            return st.context.headers.get("User-Agent", "pc")
        except:
            return "pc"

    def realizar_escaneo_web(self, user_id):
        ua = self.obtener_ua()
        ua_lower = ua.lower()
        
        # Validación estricta: Solo Android/iOS
        es_movil = any(x in ua_lower for x in ["android", "iphone", "ipad", "mobile"])
        if not es_movil:
            st.error("❌ ACCESO DENEGADO: Solo se permiten Smartphones o Tablets.")
            return

        # Detección de modelo
        modelo = "Smartphone"
        match = re.search(r'\(([^)]+)\)', ua)
        if match:
            modelo = match.group(1).split(';')[0]

        disp_id = self.model.guardar_dispositivo(user_id, modelo, "Smartphone", ua[:30])
        escaneo_id = self.model.crear_escaneo(disp_id, user_id, "Alto", 1)
        
        h = self.rules.SISTEMA_VULNS["debug_enabled"]
        with st.spinner("AnzenCore AI analizando..."):
            sugerencia = self.ai.obtener_remediacion(modelo, h['titulo'], h['nivel'])
            self.model.guardar_hallazgo(escaneo_id, "Sistema", None, h['titulo'], h['desc'], h['nivel'], sugerencia)
            st.success(f"✅ Dispositivo detectado: {modelo}")

    def obtener_historial(self, user_id):
        return self.model.obtener_historial_usuario(user_id)