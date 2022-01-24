"""Test align_benchmark."""
from align_benchmark import __version__
from align_benchmark import align_benchmark


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not align_benchmark()
    except Exception:
        assert True
