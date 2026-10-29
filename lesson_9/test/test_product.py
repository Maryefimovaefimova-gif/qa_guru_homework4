import pytest
import allure

@allure.feature("Корзина")
class TestCart:

    @pytest.mark.parametrize(
        "product",
        [
            "Курага",
            "Изюм",
            "Чеснок"
        ]
    )
    def test_add_product(self, product):

        with allure.step(f"Добавление товара {product}"):

            print(f"Добавлен товар {product}")

        assert True