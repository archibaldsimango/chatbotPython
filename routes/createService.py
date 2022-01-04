from app import app


@app.route('/create', methods=['GET'])
def create_a_service():
    return "we are creating a service"
