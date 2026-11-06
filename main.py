from flask import Flask
from controller.index_controller import index_bp
from controller.sobre_controller import sobre_bp
from controller.caracteristicas_flaskSQL_controller import caracteristicas_flaskSQL_bp
from controller.contato_controller import contato_bp
from database import engine, Base

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(sobre_bp)
app.register_blueprint(caracteristicas_flaskSQL_bp)
app.register_blueprint(contato_bp)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(port=9000, debug=True)