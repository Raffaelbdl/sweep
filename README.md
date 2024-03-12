# Sweep: A minimalist sweep tool 

![Python Version](https://img.shields.io/badge/Python->=3.10-blue)
![Code Style](https://img.shields.io/badge/Code_Style-black-black)

[**Installation**](#installation) 
| [**Example Usage**](#example-usage)

This library allows to simply evaluate all combinations of given hyperparameters.

## Installation

```bash
pip install --upgrade pip
pip install --upgrade git+https://github.com/Raffaelbdl/sweep
```

## Example Usage
```python
import sweep 

def main(cfg):
    param_A = cfg.pop("param_A", 1)
    param_B = cfg.pop("param_B", 2)

    # do stuff
    return 

if __name__ == "__main__":
    sweep_config = {
        "A": [0, 1, 2],
        "B": [0, 1, 2],
    }
    sweep.run(main, sweep_config)
```

