# Notes For Developers

These are relevant if you are making changes to classes.


## Client Config

Global configs should be stored in `config.ini`.
For client-based configs, they should be assigned as properties or attributes of the `Client` class.

## Development Setup
pip install -r requirements-dev.txt
pip install pre-commit

## Testing
pytest --cov=relevanceai tests/
