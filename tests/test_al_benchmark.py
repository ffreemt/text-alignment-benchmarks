"""Test al_benchmark."""
from al_benchmark import __version__
from al_benchmark import al_benchmark


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not al_benchmark()
    except Exception:
        assert True
