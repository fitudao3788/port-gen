# port-gen
Generate a random port within the Ephemeral Ports range  

## Installation
```bash
# Install using pip
pip install git+https://github.com/fitudao3788/port-gen

# Install using uv
uv tool install git+https://github.com/fitudao3788/port-gen
```

## Usage
```bash
$ port-gen --help
Usage: port-gen [OPTIONS] SERVICE_NAME

  Generate a random port within the Ephemeral Ports range

Options:
  --salt TEXT  Specify salt manually.
  --no-store   Don't store salt to disk.
  --help       Show this message and exit.
```