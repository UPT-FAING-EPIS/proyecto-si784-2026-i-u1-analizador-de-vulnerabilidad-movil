import os
from openai import OpenAI
import streamlit as st

class AIAdvisor:
    def __init__(self):
        # BUSCA PRIMERO EN DOKPLOY (ENV), LUEGO EN LOCAL (SECRETS)
        api_key = os.getenv("DEEPSEEK_API_KEY") or st.secrets.get("DEEPSEEK_API_KEY")
        
        self.client = OpenAI(
            api_key=api_key, 
            base_url="https://api.deepseek.com"
        )

    def obtener_remediacion(self, dispositivo, vulnerabilidad, nivel):
        prompt = f"Eres AnzenCore AI. El dispositivo {dispositivo} tiene la vulnerabilidad '{vulnerabilidad}' (Riesgo {nivel}). Explica el riesgo y da pasos para solucionarlo."
        try:
            res = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": prompt}]
            )
            return res.choices[0].message.content
        except:
            return "Sugerencia: Revise los permisos en los ajustes del sistema."