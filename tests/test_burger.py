from unittest.mock import Mock
from conftest import burger


class TestBurger:

    def test_set_buns_burger(self,burger,bun):
        burger.set_buns(bun)
        assert burger.bun.name == 'Флюоресцентная булка R2-D3'

    def test_add_ingredient_burger(self,burger,ingredient):
        burger.add_ingredient(ingredient.name)
        assert burger.ingredients == ['Соус Spicy-X']

    def test_remove_ingredient(self,burger):
        mock_ingredient = Mock()
        mock_ingredient.name = 'Соус Spicy-X'
        burger.ingredients = [mock_ingredient.name]
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self,burger):
        mock_ingredient = Mock()
        mock_ingredient.name_1 = 'Соус Spicy-X'
        mock_ingredient.name_2 = 'Мясо бессмертных моллюсков Protostomia'
        burger.ingredients = [mock_ingredient.name_1,mock_ingredient.name_2]
        burger.move_ingredient(1,0)
        assert burger.ingredients == ['Мясо бессмертных моллюсков Protostomia','Соус Spicy-X']

    def test_get_price(self,burger,bun,ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        result_price = burger.get_price()
        assert result_price == 2066

    def test_get_receipt(self,burger,bun,ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        actual_result = burger.get_receipt()
        expected_result = (
            "(==== Флюоресцентная булка R2-D3 ====)\n"
            "= sauce Соус Spicy-X =\n"
            "(==== Флюоресцентная булка R2-D3 ====)\n"
            "\n"
            "Price: 2066"
        )
        assert actual_result == expected_result

