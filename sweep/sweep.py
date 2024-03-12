import itertools as it
from multiprocessing import Process
from typing import Callable


def _create_sub_configs(sweep_config: dict) -> list[dict]:
    """Creates all combinations of sweep config dictionaries.

    Example:
        {"a": [0, 1], "b": [2]}
        => {"a": 0, "b": 2} & {"a": 1, "b": 2}
    """

    keys, values = zip(*sweep_config.items())
    return [dict(zip(keys, v)) for v in it.product(*values)]


def run(main: Callable, sweep_config: dict[str, list]) -> None:
    """Runs a sweep of all combinations of hyperparameters in a given sweep config."""

    sub_configs = _create_sub_configs(sweep_config=sweep_config)
    for config in sub_configs:
        p = Process(target=main, args=(config,))
        p.start()
        p.join()
