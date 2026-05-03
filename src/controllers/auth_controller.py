import streamlit as st
from src.models.user_model import UserModel

class AuthController:
    def __init__(self):
        self.model = UserModel()

    def login(self, nombre, password):
        user = self.model.validar(nombre, password)
        if user:
            st.session_state.user = user
            self.marcar_online(user['id'], True)
            return True
        return False

    def registrar(self, nombre, password):
        return self.model.registrar(nombre, password)

    def marcar_online(self, user_id, estado):
        try:
            self.model.actualizar_estado(user_id, estado)
        except:
            pass

    def obtener_metricas(self):
        return self.model.obtener_metricas_admin()