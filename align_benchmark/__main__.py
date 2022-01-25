"""Bootstrap."""
from itertools import zip_longest
from textwrap import wrap
from icecream import ic

from align_benchmark.benchmark import benchmark
from align_benchmark.benchmark import bm2


def main():

    # bm1

    res = round(benchmark(), 2)  # default to bm1

    indent = " " * 16
    print(" bm1 wh ch2 ".center(40))
    # print(benchmark.bench)
    # print("zip_longest:", benchmark.lst)
    print(
        "benchmark:".ljust(16),
        "\n".join(wrap(str(benchmark.bench), subsequent_indent=indent)),
    )
    print(
        "zip_longest:".ljust(16),
        "\n".join(wrap(str(benchmark.lst), subsequent_indent=indent)),
    )
    ic(res)

    # bm2
    left, right = bm2[-1]
    fillvalue = left if left < right else right
    lst = [
        *zip_longest(
            range(left + 1),
            range(right + 1),
            fillvalue=fillvalue,
        )
    ]

    res = round(benchmark(lst, bm2), 2)
    print(" bm2 wh ch1 ".center(40))
    print("benchmark:".ljust(16), "\n".join(wrap(str(bm2), subsequent_indent=indent)))
    print("zip_longest:".ljust(16), "\n".join(wrap(str(lst), subsequent_indent=indent)))
    ic(res)


if __name__ == "__main__":
    main()
