from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    
    #register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    #register fact blueprint
    from . import facts
    app.register_blueprint(facts.bp)

    return app
