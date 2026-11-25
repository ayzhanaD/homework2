from src.category import Category
from src.product import Product


def test_category_init(first_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны как средство коммуникации"
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


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


def test_category_add_product(first_category: Category) -> None:
    new_product = Product(
        name='55" QLED 4K',
        description="Фоновая подсветка",
        price=123000.0,
        quantity=7,
    )
    first_category.add_product(new_product)

    assert Category.product_count == 3
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
    )
