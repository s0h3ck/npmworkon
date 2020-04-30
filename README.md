# npmworkon

Quick script to handle nodeenv outside of the virtualenv wrapper.

If you want it in the same virtualenv wrapper, `nodeenv -p` is what you want and you don't need npmworkon.

## Installation

```
pip install npmworkon
```

The npm virtualenv will be created in the home directory `.npmvirtualenvs"`. For now, this value is hardcoded.

## Usage

Create a new virtualenv
```
$(npmworkon node_env)
```

List npm virtualenv

```
npmworkon
```

Desactivate npm virtualenv
```
deactivate_node
```
