import streamlit as st

def mostrar_login(auth_controller):
    st.markdown("<h1 class='neon-title'>ANZENCORE ACCESS</h1>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["🔐 Ingresar", "📝 Registrarse"])
    
    with tab1:
        u = st.text_input("Usuario", key="l_u").strip().lower()
        p = st.text_input("Contraseña", type="password", key="l_p")
        if st.button("ACCEDER"):
            if auth_controller.login(u, p):
                st.rerun()
            else:
                st.error("Credenciales incorrectas.")
                
    with tab2:
        u_r = st.text_input("Nuevo Usuario", key="r_u").strip().lower()
        p_r = st.text_input("Nueva Contraseña", type="password", key="r_p")
        if st.button("CREAR CUENTA"):
            if u_r and p_r:
                auth_controller.registrar(u_r, p_r)
                st.success(f"Usuario {u_r} creado. Ingrese en la otra pestaña.")