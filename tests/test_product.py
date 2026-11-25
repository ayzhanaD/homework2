import pytest

from src.product import Product


def test_product_init(first_product: Product) -> None:
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_new_product() -> None:
    product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14,
    }
    new_prod = Product.new_product(product_data)
    assert isinstance(new_prod, Product)
    assert new_prod.name == "Xiaomi Redmi Note 11"
    assert new_prod.description == "1024GB, Синий"
    assert new_prod.price == 31000.0
    assert new_prod.quantity == 14


def test_price_setter_positive(first_product: Product) -> None:
    first_product.price = 150000.0
    assert first_product.price == 150000.0


def test_price_setter_invalid(first_product: Product, capsys: pytest.CaptureFixture) -> None:
    first_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert first_product.price == 180000.0

    first_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert first_product.price == 180000.0
