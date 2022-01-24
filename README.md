# text-alignment-benchmarks
[![tests](https://github.com/ffreemt/text-alignment-benchmarks/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/text-alignment-benchmarks/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/al_benchmark.svg)](https://badge.fury.io/py/al_benchmark)

Benchmark dualtext (para/sent) alignment

## Install it

```shell
pip install al-benchmark
# or poetry add al-benchmark
# pip install git+htts://github.com/ffreemt/text-alignment-benchmarks
# poetry add git+htts://github.com/ffreemt/text-alignment-benchmarks

# To upgrade
pip install al-benchmark -U
# or poetry add al-benchmark@latest
```

## Use it
```python
from al_benchmark.benchmark import benchmark

benchmark()

```
