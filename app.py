from flask import Flask

from services.inventory_service import inventory_services_bp

app = Flask(__name__)

# Enregistrer le Blueprint
app.register_blueprint(inventory_services_bp)

if __name__ == '__main__':
    app.run(debug=True)
