from store.usecases.product import product_usecase
from tests.factories import product_data

async def test_usecases_should_return_success(product_in):
    result = await product_usecase.create(body=product_data())

    assert isinstance(result,ProductOut)
    assert result.name == "iPhone 14 Pro Max"