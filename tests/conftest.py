import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app(testing=True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_planets():
    earth = Planet(name="Earth",description="It has water", radius=2456)
    venus = Planet(name="Venus", description="The love planet", radius=3456)

    db.session.add_all([earth,venus])
    db.session.commit()