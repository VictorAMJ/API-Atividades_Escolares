from flask import Flask
from config import app, db
from rotasAtividade import atividade

app.register_blueprint(atividade)

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
        )
    