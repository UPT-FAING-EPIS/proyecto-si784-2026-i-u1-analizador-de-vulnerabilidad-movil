import streamlit as st
import pandas as pd
import os
import base64

class AnzenView:
    # Función auxiliar para forzar la descarga en móviles
    def get_apk_download_link(self, apk_path, filename):
        with open(apk_path, "rb") as f:
            bytes = f.read()
            b64 = base64.b64encode(bytes).decode()
        
        # Estilo CSS para que parezca un botón de Streamlit
        button_style = """
            <style>
                .descargar-btn {
                    background-color: #ff4b4b;
                    color: white !important;
                    padding: 0.5em 1em;
                    text-decoration: none;
                    border-radius: 10px;
                    border: none;
                    font-weight: bold;
                    display: inline-block;
                    text-align: center;
                }
                .descargar-btn:hover {
                    background-color: #ff3333;
                }
            </style>
        """
        href = f'{button_style}<a href="data:application/vnd.android.package-archive;base64,{b64}" download="{filename}" class="descargar-btn">⬇️ Descargar AnzenCore APK</a>'
        return href

    def render_login(self):
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
        
        return u, p, btn, ru, rp, rbtn

    def render_dashboard(self, user, online_users, reports):
        st.title("🚀 AnzenCore Live Dashboard")
        
        c1, c2, c3 = st.columns([1, 1, 1.5])
        c1.metric("Online", len(online_users))
        c2.info(f"Sesión: {user['username']}")
        
        with c3:
            st.write("📲 **Herramienta de Precisión**")
            apk_path = "assets/AnzenCore_Agent.apk"
            if os.path.exists(apk_path):
                # USAMOS EL NUEVO MÉTODO HTML AQUÍ
                st.markdown(self.get_apk_download_link(apk_path, "AnzenCore.apk"), unsafe_allow_html=True)
            else:
                st.error("Archivo APK no encontrado en /assets")

        st.subheader("👥 Usuarios conectados")
        # Mostrar usuarios como badges
        user_list = [f"🟢 `{u['username']}`" for u in online_users]
        st.write(" ".join(user_list))
        
        st.divider()
        st.subheader("📊 Historial de Vulnerabilidades")
        if reports:
            df = pd.DataFrame(reports)
            # Limpiar y mostrar tabla
            df_display = df[['dispositivo', 'vulnerabilidad', 'nivel', 'fecha']].copy()
            st.dataframe(df_display, use_container_width=True)
        else:
            st.info("Esperando reportes del Agente Móvil...")