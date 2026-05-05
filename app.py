import streamlit as st
from streamlit_autorefresh import st_autorefresh
from src.models import AnzenModel
from src.controllers import AnzenController
from src.views import AnzenView

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="AnzenCore: Mobile Security",
    page_icon="🛡️",
    layout="wide"
)

# 2. INICIALIZACIÓN DEL PATRÓN MVC EN SESIÓN
# Esto evita que los objetos se creen de nuevo en cada refresco
if 'model' not in st.session_state:
    st.session_state.model = AnzenModel()
    st.session_state.controller = AnzenController(st.session_state.model)
    st.session_state.view = AnzenView()

m = st.session_state.model
c = st.session_state.controller
v = st.session_state.view

def main():
    # --- FLUJO DE AUTENTICACIÓN ---
    if 'user' not in st.session_state:
        # Llamamos a la vista de login que devuelve los inputs y botones de las pestañas
        u, p, b, ru, rp, rb = v.render_login()
        
        if b: # Botón de Login presionado
            user = c.login(u, p)
            if user:
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Credenciales incorrectas. Intente de nuevo.")
        
        if rb: # Botón de Registro presionado
            if ru and rp:
                if c.signup(ru, rp):
                    st.success("✅ Usuario registrado exitosamente. Ya puede ingresar.")
                else:
                    st.error("❌ El nombre de usuario ya existe.")
            else:
                st.warning("Por favor, complete todos los campos.")

    # --- FLUJO DE DASHBOARD (USUARIO AUTENTICADO) ---
    else:
        # A. TIEMPO REAL: Refrescar la página cada 5 segundos para actualizar el monitor
        st_autorefresh(interval=5000, key="refresh_dashboard")
        
        # B. HEARTBEAT: Avisar a Supabase que el usuario sigue con la web abierta
        m.update_ping(st.session_state.user['id'])
        
        # C. OBTENER DATOS ACTUALIZADOS
        online_users = c.fetch_online_list()
        reports = c.fetch_all_reports()
        
        # D. BARRA LATERAL (SIDEBAR)
        st.sidebar.markdown(f"## 👤 Perfil")
        st.sidebar.write(f"**Usuario:** {st.session_state.user['username']}")
        
        # El ID es vital para que el usuario lo escriba en el APK móvil
        st.sidebar.info(f"🔑 **Tu ID AnzenCore:** \n\n `{st.session_state.user['id']}`")
        
        if st.sidebar.button("Cerrar Sesión"):
            del st.session_state.user
            st.rerun()
        
        st.sidebar.divider()
        st.sidebar.caption("AnzenCore v1.0 - Análisis de Vulnerabilidades")

        # E. RENDERIZAR DASHBOARD PRINCIPAL
        v.render_dashboard(
            st.session_state.user, 
            online_users, 
            reports
        )

if __name__ == "__main__":
    main()