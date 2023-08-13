from flask import Flask

def create_app():
    # Create a new Flask app instance
    app = Flask(__name__)

    # Import the pet blueprint
    from . import pet

# Define a basic index route for the main app
    @app.route('/')
    def main_index():
        return 'Hello, PetFax! This is the main index.'
    # Register pet blueprint
    app.register_blueprint(pet.bp)
    
    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)


    return app
