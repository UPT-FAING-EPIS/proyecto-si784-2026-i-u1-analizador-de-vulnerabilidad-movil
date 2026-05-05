# app.py
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from src.models import AnzenModel
from src.controllers import AnzenController
from src.views import AnzenView

st.set_page_config(page_title="AnzenCore", layout="wide")

# Inicializar componentes en la sesión
if 'model' not in st.session_state:
    st.session_state.model = AnzenModel()
    st.session_state.controller = AnzenController(st.session_state.model)
    st.session_state.view = AnzenView() # Guardamos la vista en sesión

m = st.session_state.model
c = st.session_state.controller
v = st.session_state.view

def main():
    if 'user' not in st.session_state:
        # Aquí es donde daba el error: ahora coinciden los 6 valores
        u, p, b, ru, rp, rb = v.render_login()
        
        if b:
            usr = c.login(u, p)
            if usr:
                st.session_state.user = usr
                st.rerun()
            else:
                st.error("Usuario o clave incorrectos")
        
        if rb:
            if c.signup(ru, rp):
                st.success("¡Registrado! Ya puedes ingresar.")
            else:
                st.error("Error: El usuario ya existe.")
    else:
        # Refresco automático solo cuando ya están logueados
        st_autorefresh(interval=5000, key="refresh")
        
        m.update_ping(st.session_state.user['id']) # Reportar presencia
        online = c.get_live_users()
        reports = c.get_vulnerabilities()
        
        if st.sidebar.button("Cerrar Sesión"):
            del st.session_state.user
            st.rerun()
            
        v.render_dashboard(st.session_state.user, online, reports)

if __name__ == "__main__":
    main()