import pytest
from app.model.input_config_model import InputDataModelFromConfig
def test_input():
    InputDataModelFromConfig('Configurations.ini')