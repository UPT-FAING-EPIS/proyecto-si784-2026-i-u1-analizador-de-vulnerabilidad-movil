from datetime import datetime, timedelta

class AnzenController:
    def __init__(self, model):
        self.model = model

    def login(self, u, p):
        res = self.model.auth_user(u, p)
        return res.data[0] if res.data else None

    def signup(self, u, p):
        try:
            self.model.register_user(u, p)
            return True
        except: return False

    def get_live_users(self):
        # Umbral de 30 segundos para tiempo real
        limit = (datetime.now() - timedelta(seconds=30)).isoformat()
        return self.model.get_online_users(limit).data

    def get_vulnerabilities(self):
        return self.model.get_reports().data