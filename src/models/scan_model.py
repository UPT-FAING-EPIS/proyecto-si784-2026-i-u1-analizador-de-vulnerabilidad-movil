from src.models.db_manager import DBManager
import pandas as pd

class ScanModel:
    def __init__(self):
        self.db = DBManager()

    def guardar_dispositivo(self, user_id, nombre, tipo, os):
        query = """
            INSERT INTO dispositivos (usuario_id, nombre_modelo, tipo, os_version)
            VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO UPDATE SET ultima_auditoria=NOW() RETURNING id
        """
        res = self.db.ejecutar_query(query, (user_id, nombre, tipo, os), es_select=True)
        return res[0]['id'] if res else None

    def crear_escaneo(self, disp_id, user_id, riesgo, total):
        query = "INSERT INTO escaneos (dispositivo_id, usuario_id, riesgo_global, total_vulnerabilidades) VALUES (%s, %s, %s, %s) RETURNING id"
        res = self.db.ejecutar_query(query, (disp_id, user_id, riesgo, total), es_select=True)
        return res[0]['id'] if res else None

    def guardar_hallazgo(self, escaneo_id, cat, app, titulo, desc, nivel, sugerencia):
        query = """
            INSERT INTO hallazgos_seguridad (escaneo_id, categoria, app_nombre, titulo_vulnerabilidad, descripcion, nivel, sugerencia_solucion)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.db.ejecutar_query(query, (escaneo_id, cat, app, titulo, desc, nivel, sugerencia))

    def obtener_historial_usuario(self, user_id):
        query = """
            SELECT e.fecha_inicio, d.nombre_modelo, e.riesgo_global, e.total_vulnerabilidades 
            FROM escaneos e JOIN dispositivos d ON e.dispositivo_id = d.id 
            WHERE e.usuario_id = %s ORDER BY e.fecha_inicio DESC
        """
        data = self.db.ejecutar_query(query, (user_id,), es_select=True)
        return pd.DataFrame(data) if data else None