from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Evento
class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    local = db.Column(db.String(100))
    categoria = db.Column(db.String(50))

# Criação do banco de dados
with app.app_context():
    db.create_all()

# Função auxiliar para converter evento em dicionário
def evento_to_dict(evento):
    return {
        'id': evento.id,
        'nome': evento.nome,
        'descricao': evento.descricao,
        'data_hora': evento.data_hora.isoformat(),
        'local': evento.local,
        'categoria': evento.categoria
    }

# Endpoint GET /eventos
@app.route('/eventos', methods=['GET'])
def get_eventos():
    categoria = request.args.get('categoria')
    data = request.args.get('data')
    quantidade = request.args.get('quantidade', type=int, default=10)
    ordering = request.args.get('ordering', default='data_hora')
    
    query = Evento.query
    
    if categoria:
        query = query.filter(Evento.categoria == categoria)
    if data:
        data_obj = datetime.strptime(data, '%Y-%m-%d')
        query = query.filter(Evento.data_hora.date() == data_obj.date())
    
    eventos = query.order_by(getattr(Evento, ordering)).limit(quantidade).all()
    
    return jsonify([evento_to_dict(evento) for evento in eventos])

# Endpoint POST /eventos
@app.route('/eventos', methods=['POST'])
def create_evento():
    data = request.get_json()
    nome = data.get('nome')
    descricao = data.get('descricao')
    data_hora = datetime.strptime(data.get('data_hora'), '%Y-%m-%dT%H:%M:%S')
    local = data.get('local')
    categoria = data.get('categoria')
    
    novo_evento = Evento(nome=nome, descricao=descricao, data_hora=data_hora, local=local, categoria=categoria)
    
    db.session.add(novo_evento)
    db.session.commit()
    
    return jsonify(evento_to_dict(novo_evento)), 201

# Endpoint PUT /eventos/{id}
@app.route('/eventos/<int:id>', methods=['PUT'])
def update_evento(id):
    evento = Evento.query.get_or_404(id)
    
    data = request.get_json()
    evento.nome = data.get('nome', evento.nome)
    evento.descricao = data.get('descricao', evento.descricao)
    evento.data_hora = datetime.strptime(data.get('data_hora'), '%Y-%m-%dT%H:%M:%S') if data.get('data_hora') else evento.data_hora
    evento.local = data.get('local', evento.local)
    evento.categoria = data.get('categoria', evento.categoria)
    
    db.session.commit()
    
    return jsonify(evento_to_dict(evento))

# Endpoint DELETE /eventos/{id}
@app.route('/eventos/<int:id>', methods=['DELETE'])
def delete_evento(id):
    evento = Evento.query.get_or_404(id)
    db.session.delete(evento)
    db.session.commit()
    
    return jsonify({'message': 'Evento deletado com sucesso!'})

# Endpoint GET /eventos/proximos
@app.route('/eventos/proximos', methods=['GET'])
def eventos_proximos():
    hoje = datetime.now()
    data_futura = hoje + timedelta(days=7)
    eventos = Evento.query.filter(Evento.data_hora > hoje, Evento.data_hora <= data_futura).all()
    
    return jsonify([evento_to_dict(evento) for evento in eventos])

# Endpoint GET /eventos/{id}
@app.route('/eventos/<int:id>', methods=['GET'])
def get_evento(id):
    evento = Evento.query.get_or_404(id)
    return jsonify(evento_to_dict(evento))

# Executando a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5000/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Eventos"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

from flask import send_from_directory

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


