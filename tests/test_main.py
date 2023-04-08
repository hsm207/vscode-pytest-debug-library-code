import pytest
from main import create_id

def test_create_id():
    obj = {
        "text": "Hello World",
    }

    obj_id = create_id(obj)

    assert isinstance(obj_id, str)