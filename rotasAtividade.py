from flask import Blueprint, request, jsonify
from datetime import date, datetime
from config import db
from modelAtividade import (
    AtividadeNaoEncontrada,
    model_post_atividade,
    model_get_atividade,
)

atividade = Blueprint('atividade', __name__)

@atividade.route("/atividade", methods=["POST"])
def post_atividade():
    try:
        dados_atividade = request.json
        print(f"dados coletados: {dados_atividade}")
        resposta, status_code = model_post_atividade(dados_atividade)
        return jsonify(resposta), status_code
    except Exception as e:
        return jsonify({"erro": f"Erro inseperado ao criar atividade: {str(e)}"}), 500
    

@atividade.route("/atividade", methods=["GET"])
def get_atividade():
    try:
        atividades = model_get_atividade()
        return jsonify(atividades)
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado ao listar as atividades: {str(e)}"}), 500
    
