# src/views.py
import streamlit as st
import pandas as pd
import os

class AnzenView:
    def render_login(self): # Quitamos el @staticmethod para evitar conflictos
        st.title("🛡️ AnzenCore Access")
        tab1, tab2 = st.tabs(["Ingreso", "Registro"])
        
        with tab1:
            u = st.text_input("Usuario", key="l_u")
            p = st.text_input("Contraseña", type="password", key="l_p")
            btn = st.button("Iniciar Sesión")
        with tab2:
            ru = st.text_input("Nuevo Usuario", key="r_u")
            rp = st.text_input("Nueva Contraseña", type="password", key="r_p")
            rbtn = st.button("Crear Cuenta")
        
        # Retornamos los 6 valores que app.py espera
        return u, p, btn, ru, rp, rbtn

    def render_dashboard(self, user, online_users, reports):
        st.title("🚀 AnzenCore Live Dashboard")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Online", len(online_users))
        c2.info(f"Sesión: {user['username']}")
        
        with c3:
            st.write("📲 **Herramienta**")
            if os.path.exists("assets/AnzenCore_Agent.apk"):
                with open("assets/AnzenCore_Agent.apk", "rb") as f:
                    st.download_button("Descargar APK", f, file_name="AnzenCore.apk")
            else:
                st.button("APK no disponible", disabled=True)

        st.subheader("👥 Usuarios conectados")
        st.write(", ".join([f"🟢 `{u['username']}`" for u in online_users]))
        
        st.divider()
        st.subheader("📊 Historial de Vulnerabilidades")
        if reports:
            df = pd.DataFrame(reports)
            st.dataframe(df[['dispositivo', 'vulnerabilidad', 'nivel', 'fecha']], use_container_width=True)