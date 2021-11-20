from flask import Flask
from API_usuarios import usuarios_app
from API_produtos import produtos_app
from API_estoque import estoque_app

app = Flask(__name__)
app.register_blueprint(usuarios_app)
app.register_blueprint(produtos_app)
app.register_blueprint(estoque_app)
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_DB'] = 'artes'
# app.config['MYSQL_DATABASE_Host']='127.0.0.1:3306'
# mysql=MySQL(app)

if __name__ == '__main__':
    # subprocess.Popen("analise_banco_dados.py", shell=True)
    app.run(host='localhost', port=5000, debug=True)
