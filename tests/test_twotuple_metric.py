"""Test twotuple_metric."""
# pylint: disable=invalid-name

from pathlib import Path
from itertools import zip_longest

import pandas as pd

from align_benchmark.twotuple_metric import twotuple_metric


file_loc = "data/para-wh-ch2-benchmark1.xlsx"
if not Path(file_loc).exists():
    raise SystemExit(f"File [{file_loc}] does not exist.")

_ = pd.read_excel(file_loc, header=0)[["Unnamed: 1", "Unnamed: 3"]]
_.columns = ["list1", "list2"]
bm1 = _.to_numpy().tolist()

lst = [*zip_longest(range(33), range(36), fillvalue=32)]


def test_twotuple_metric55():
    """Test twotuple_metric 5 5."""
    assert twotuple_metric(bm1[5], lst[5]) == 0.5


def test_twotuple_metric_nonnumerical_entry():
    """Test entry that cannot be converted to integer."""
    assert twotuple_metric([0, 1], [0, ""]) == 0.0
