import streamlit as st
import plotly.express as px
import pandas as pd
from src.views.theme import draw_card

def mostrar_dashboard_admin(auth_controller):
    st.markdown("<h1 class='neon-title'>ADMIN TELEMETRY</h1>", unsafe_allow_html=True)
    
    m = auth_controller.obtener_metricas()
    if m:
        data = m[0]
        # Fila de métricas con diseño Card
        c1, c2, c3, c4 = st.columns(4)
        with c1: draw_card("Usuarios Online", data['usuarios_online'])
        with c2: draw_card("Escaneando", data['usuarios_activos'], "#ffeb3b")
        with c3: draw_card("Auditorías Totales", data['total_analisis_realizados'])
        with c4: draw_card("Amenazas Críticas", data['alertas_criticas'], "#ff4b4b")

        st.write("---")
        
        # Gráfico circular neón
        df_plot = pd.DataFrame({
            "Estado": ["Seguros", "Críticos"],
            "Cantidad": [data['total_analisis_realizados'] - data['alertas_criticas'], data['alertas_criticas']]
        })
        fig = px.pie(df_plot, values='Cantidad', names='Estado', hole=0.5, 
                     color_discrete_map={'Seguros':'#00d4ff','Críticos':'#ff4b4b'},
                     title="Distribución Global de Riesgos")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Error al cargar telemetría.")