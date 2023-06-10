from flask import Flask, request
from flask_restful import Resource, Api
from functools import wraps

app = Flask(__name__)
api = Api(app)

# Dicionário simulando um banco de dados de usuários
users = {
    "john": "password1",
    "jane": "password2"
}

# Função para verificar o token de autenticação


def authenticate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            # Verificar o token aqui (pode ser um processo mais complexo)
            return func(*args, **kwargs)
        else:
            return {'message': 'Token de autenticação não fornecido.'}, 401
    return decorated

# Classe para o endpoint /user


class User(Resource):
    @authenticate
    def get(self):
        return {'message': 'Endpoint /user chamado com sucesso.'}

# Classe para o endpoint /dashboard


class Dashboard(Resource):
    @authenticate
    def get(self):
        return {'message': 'Endpoint /dashboard chamado com sucesso.'}

# Classe para o endpoint /login


class Login(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')

        if username in users and password == users[username]:
            # Lógica de geração do token de autenticação
            token = 'token_gerado_aqui'
            return {'token': token}
        else:
            return {'message': 'Credenciais inválidas.'}, 401

# Classe para o endpoint /logoff


class Logoff(Resource):
    @authenticate
    def post(self):
        # Lógica de invalidação do token de autenticação
        return {'message': 'Usuário deslogado com sucesso.'}

# Classe para o endpoint /report


class Report(Resource):
    @authenticate
    def get(self):
        return {'message': 'Endpoint /report chamado com sucesso.'}

# Classe para o endpoint /health


class Health(Resource):
    def get(self):
        return {'status': 'OK'}


# Adicionar os recursos/endpoints à API
api.add_resource(User, '/user')
api.add_resource(Dashboard, '/dashboard')
api.add_resource(Login, '/login')
api.add_resource(Logoff, '/logoff')
api.add_resource(Report, '/report')
api.add_resource(Health, '/health')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
