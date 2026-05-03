import bcrypt
from src.models.db_manager import DBManager

class UserModel:
    def __init__(self):
        self.db = DBManager()

    def registrar(self, nombre, password, rol_id=2):
        nombre_limpio = nombre.strip().lower()
        salt = bcrypt.gensalt()
        # Hashear y decodificar a string para guardarlo en Postgres
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
        
        query = "INSERT INTO usuarios (nombre, password_hash, rol_id) VALUES (%s, %s, %s)"
        return self.db.ejecutar_query(query, (nombre_limpio, hashed_pw, rol_id))

    def validar(self, nombre, password):
        nombre_limpio = nombre.strip().lower()
        query = "SELECT id, nombre, password_hash, rol_id FROM usuarios WHERE nombre = %s"
        res = self.db.ejecutar_query(query, (nombre_limpio,), es_select=True)
        
        if res:
            user = res[0]
            # Comparamos la clave plana con el hash (ambos convertidos a bytes)
            if bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
                return user
        return None

    def actualizar_estado(self, user_id, online, escaneando=False):
        query = "UPDATE usuarios SET esta_en_linea=%s, esta_escaneando=%s, ultima_actividad=NOW() WHERE id=%s"
        self.db.ejecutar_query(query, (online, escaneando, user_id))
    
    def obtener_metricas_admin(self):
        query = "SELECT * FROM dashboard_admin_stats"
        return self.db.ejecutar_query(query, es_select=True)