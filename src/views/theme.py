import streamlit as st

def aplicar_estilo_personalizado():
    st.markdown("""
        <style>
        /* Fondo y tipografía */
        .main {
            background-color: #0e1117;
            color: #ffffff;
        }
        
        /* Botones estilo Neón */
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            height: 3.5em;
            background-color: #007bff;
            color: white;
            border: 1px solid #00d4ff;
            transition: 0.3s;
            font-weight: bold;
        }
        .stButton>button:hover {
            box-shadow: 0px 0px 20px #00d4ff;
            background-color: #0056b3;
            transform: scale(1.02);
        }

        /* Cards para métricas */
        .card {
            background-color: #1a1c24;
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #333;
            text-align: center;
            margin-bottom: 15px;
        }

        /* Títulos con sombra neón */
        .neon-title {
            color: #ffffff;
            text-shadow: 0 0 10px #00d4ff, 0 0 20px #00d4ff;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #111318;
            border-right: 1px solid #00d4ff;
        }
        </style>
    """, unsafe_allow_html=True)

def draw_card(title, value, color="#00d4ff"):
    st.markdown(f"""
        <div class="card">
            <p style="color: #888; font-size: 14px; margin: 0;">{title}</p>
            <h2 style="color: {color}; margin: 5px 0;">{value}</h2>
        </div>
    """, unsafe_allow_html=True)