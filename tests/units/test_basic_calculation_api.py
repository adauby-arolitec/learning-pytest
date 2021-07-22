from app import create_app
from pytest import fixture

@fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_calculation_api(client):
    res = client.get("/calculation").status_code == 200