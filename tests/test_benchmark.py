"""Test benchmark."""
from icecream import ic

from al_benchmark.benchmark import benchmark


def test_benchmark_mat_55():
    """Test benchmark mat[5, 5]."""
    benchmark()

    ic(benchmark.mat[5, 5])

    assert benchmark.mat[5, 5] == 0.5
