import streamlit as st
from src.views.theme import draw_card

def mostrar_dashboard_usuario(usuario, scan_controller):
    st.markdown(f"<h1 class='neon-title'>SECURITY TERMINAL</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #00d4ff;'>Dispositivo Vinculado a: <b>{usuario['nombre'].upper()}</b></p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
            <div style='background-color: #1a1c24; padding: 20px; border-radius: 15px; border: 1px solid #00d4ff;'>
                <h3 style='color: white;'>Audit Tool</h3>
                <p style='color: #888;'>Ejecute un escaneo profundo para detectar brechas de seguridad.</p>
            </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("🚀 INICIAR ESCANEO"):
            scan_controller.realizar_escaneo_web(usuario['id'])
            st.balloons()

    with col2:
        st.subheader("📜 Historial de Auditorías")
        hist = scan_controller.obtener_historial(usuario['id'])
        if hist is not None and not hist.empty:
            st.dataframe(hist, use_container_width=True)
        else:
            st.info("Sin registros de auditoría en esta cuenta.")