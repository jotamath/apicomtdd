from uuid import UUID

from pydantic import ValidationError
import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data, product_missing_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "iPhone 14 Pro Max"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = product_missing_data()
    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)
    
    assert err.value.errors()[0] == {'type': 'missing', 'loc': ('status',), 'msg': 'Field required', 'input': {'name': 'iPhone 14 Pro Max', 'quantity': 10, 'price': 6500}, 'url': 'https://errors.pydantic.dev/2.9/v/missing'}