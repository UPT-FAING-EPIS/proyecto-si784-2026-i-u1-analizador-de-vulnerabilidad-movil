import psycopg2
import streamlit as st
from psycopg2.extras import RealDictCursor

class DBManager:
    def __init__(self):
        try:
            # Cargamos la URL directamente del Secret
            self.db_url = st.secrets["DB_URL"]
        except Exception:
            st.error("❌ Error: No se encontró la variable DB_URL en los Secrets.")
            st.stop()

    def ejecutar_query(self, query, params=None, es_select=False):
        resultado = None
        conn = None
        try:
            # Abrimos la conexión (El puerto 6543 nos permite usar IPv4)
            conn = psycopg2.connect(self.db_url)
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                if es_select:
                    resultado = cur.fetchall()
                conn.commit()
        except Exception as e:
            if conn: conn.rollback()
            st.error(f"Error de base de datos: {e}")
        finally:
            # CERRAMOS SIEMPRE: Vital para no agotar las conexiones del plan gratuito
            if conn:
                conn.close()
        return resultado