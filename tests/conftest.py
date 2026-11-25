import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product() -> Product:
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product() -> Product:
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
    )


@pytest.fixture
def first_category(first_product: Product, second_product: Product) -> Category:
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        name="Смартфоны",
        description="Смартфоны как средство коммуникации",
        products=[first_product, second_product],
    )
