import os
import psycopg2
import streamlit as st
from psycopg2.extras import RealDictCursor

class DBManager:
    def __init__(self):
        # BUSCA PRIMERO EN DOKPLOY (ENV), LUEGO EN LOCAL (SECRETS)
        self.db_url = os.getenv("DB_URL") or st.secrets.get("DB_URL")

    @st.cache_resource
    def _obtener_conexion(_self):
        # Mantiene la conexión abierta para mayor velocidad
        return psycopg2.connect(_self.db_url, sslmode='require')

    def ejecutar_query(self, query, params=None, es_select=False):
        conn = self._obtener_conexion()
        resultado = None
        try:
            # Si la conexión se cae, forzar reconexión
            if conn.closed:
                st.cache_resource.clear()
                conn = self._obtener_conexion()

            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                if es_select:
                    resultado = cur.fetchall()
                conn.commit()
        except Exception as e:
            if not conn.closed: conn.rollback()
            st.cache_resource.clear() # Limpiar caché en caso de error crítico
        return resultado