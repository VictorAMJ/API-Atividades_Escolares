import requests
from config import db
from datetime import date, datetime

url_professor = "http://localhost:8080/professor/"

class Atividade(db.Model):
    __tablename__ = "atividade"
    
    id_atividade = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(400), nullable=False)
    data_entrega = db.Column(db.Date, nullable=False)
    id_professor = db.Column(db.Integer, nullable=False)
    nota_maxima = db.Column(db.Integer, default=10)
    
    def __init__(self, enunciado, data_entrega, id_professor, nota_maxima=10):
        self.enunciado = enunciado
        self.data_entrega = data_entrega
        self.id_professor = id_professor
        self.nota_maxima = nota_maxima
    
    def transforma_em_dici(self):
        return {
            'id_atividade': self.id_atividade,
            'enunciado': self.enunciado,
            'data_entrega': self.data_entrega.isoformat(),
            'id_professor': self.id_professor,
            'nota_maxima': self.nota_maxima
        }
        
class AtividadeNaoEncontrada(Exception):
    pass

class ProfessorNaoEncontrado(Exception):
    pass


def professor_existe(id_professor):
    resposta = requests.get(f"{url_professor}{id_professor}")
    if resposta.status_code != 200:
        raise ProfessorNaoEncontrado(f"ID {id_professor} não encontrado em Professor")

    
def model_post_atividade(dados_atividade):
    professor_existe(dados_atividade["id_professor"])
    
    nova_atividade = Atividade(
        enunciado= dados_atividade["enunciado"],
        data_entrega= datetime.strptime(dados_atividade["data_entrega"], "%Y-%m-%d").date(),
        id_professor= dados_atividade["id_professor"],
        nota_maxima= dados_atividade.get("nota_maxima", 10)
    )
    
    db.session.add(nova_atividade)
    db.session.commit()
    return {"mensagem": "Atividade adicionada com sucesso!"}, 201

    
def model_get_atividade():
    atividades = Atividade.query.all()
    print(atividades)
    return [atividade.transforma_em_dici() for atividade in atividades]

