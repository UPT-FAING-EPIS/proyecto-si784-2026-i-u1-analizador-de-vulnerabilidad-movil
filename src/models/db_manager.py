import psycopg2
import streamlit as st
from psycopg2.extras import RealDictCursor

class DBManager:
    def __init__(self):
        try:
            self.db_url = st.secrets["DB_URL"]
        except Exception:
            st.error("❌ Error: No se encontró DB_URL en los Secrets.")
            st.stop()

    def conectar(self):
        # Conexión directa a través del Pooler (Puerto 6543)
        return psycopg2.connect(self.db_url)

    def ejecutar_query(self, query, params=None, es_select=False):
        resultado = None
        conn = None
        try:
            conn = self.conectar()
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                if es_select:
                    resultado = cur.fetchall()
                conn.commit()
        except Exception as e:
            if conn: conn.rollback()
            st.error(f"Error de comunicación con la base de datos: {e}")
        finally:
            if conn:
                conn.close()
        return resultado