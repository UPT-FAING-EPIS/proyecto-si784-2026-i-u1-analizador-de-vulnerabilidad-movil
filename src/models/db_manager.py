import psycopg2
import streamlit as st
from psycopg2.extras import RealDictCursor

class DBManager:
    def __init__(self):
        try:
            self.db_url = st.secrets["DB_URL"]
        except Exception:
            st.error("❌ Error: No se encontró la variable DB_URL en los Secrets de Streamlit.")
            st.stop()

    def conectar(self):
        """Crea una conexión limpia a la base de datos"""
        return psycopg2.connect(self.db_url)

    def ejecutar_query(self, query, params=None, es_select=False):
        resultado = None
        conn = None
        try:
            # 1. Abrir conexión
            conn = self.conectar()
            
            # 2. Ejecutar consulta
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                if es_select:
                    resultado = cur.fetchall()
                conn.commit()
            
            return resultado
            
        except Exception as e:
            if conn: conn.rollback()
            st.error(f"⚠️ Error de base de datos: {e}")
            return None
            
        finally:
            # 3. CERRAR SIEMPRE: Crítico para que el pooler de Supabase no se bloquee
            if conn:
                conn.close()