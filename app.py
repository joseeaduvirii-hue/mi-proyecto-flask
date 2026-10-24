from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Usuario

app = Flask(__name__)

# Configuración de la base de datos local SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return jsonify({"mensaje": "¡Aplicación con Flask y Migraciones configurada con éxito!"})

if __name__ == '__main__':
    app.run(debug=True)