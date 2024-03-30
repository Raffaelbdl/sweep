from dataclasses import Field
import itertools as it
from multiprocessing import Process
from typing import Any, Callable, TypeVar

Dataclass = TypeVar("Dataclass")

from shaberax.logger import GeneralLogger


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


def _check_in_fields(attr: str, fields: dict[str, Field]) -> bool:
    return attr in fields


def _check_value_type(attr: str, value: Any, fields: dict[str, Field]) -> bool:
    return type(value) is fields[attr].type


def override(config: Dataclass, override_config: dict) -> Dataclass:
    """Overrides a Dataclass config with the sweep ones."""
    fields = config.__dataclass_fields__
    for k, v in override_config.items():
        if not _check_in_fields(k, fields):
            raise AttributeError(f"{k} is not a valid config key.")
        if not _check_value_type(k, v, fields):
            GeneralLogger.warning(
                f"{k} does not have a valid Type for value {v}.\n Process not stopped."
            )
        config.__setattr__(k, v)
    return config
