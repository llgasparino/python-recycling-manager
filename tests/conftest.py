import pytest
from recycling_manager import app as flask_app


@pytest.fixture()
def app():
    """Flask app configured for testing."""
    flask_app.config.update(TESTING=True)
    yield flask_app


@pytest.fixture()
def client(app):
    """Flask test client."""
    return app.test_client()
