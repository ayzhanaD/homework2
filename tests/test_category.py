from src.category import Category
from src.product import Product


def test_category_init(first_category: Category, first_product: Product, second_product: Product) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны как средство коммуникации"
    assert first_category.products == [first_product, second_product]


def test_category_counters(first_category: Category, first_product: Product) -> None:
    assert Category.category_count == 1
    assert Category.product_count == 2
    assert first_category.category_count == 1
    assert first_category.product_count == 2

    second_category = Category(
        name="Телевизоры",
        description="Современные телевизоры",
        products=[first_product],
    )
    assert Category.category_count == 2
    assert Category.product_count == 3
    assert second_category.category_count == 2
    assert second_category.product_count == 3
