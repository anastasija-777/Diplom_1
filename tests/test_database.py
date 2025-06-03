import pytest
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE,INGREDIENT_TYPE_FILLING


class TestDataBase:

    @pytest.mark.parametrize('value',[
        [["black bun", 100],["white bun", 200],["red bun", 300]],
        []
    ]
                             )
    def test_available_buns(self,value):
        mock_data_base = Mock()
        mock_data_base.buns = value
        buns = Database.available_buns(mock_data_base)
        assert buns == value


    @pytest.mark.parametrize('value', [
        [],
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [[INGREDIENT_TYPE_SAUCE, "hot sauce", 100], [INGREDIENT_TYPE_SAUCE, "sour cream", 200],[INGREDIENT_TYPE_SAUCE, "chili sauce", 300],[INGREDIENT_TYPE_FILLING, "cutlet", 100], [INGREDIENT_TYPE_SAUCE, "sour cream", 200],[INGREDIENT_TYPE_FILLING, "sausage", 300]]
    ]
                             )
    def test_available_ingredients(self, value):
        mock_data_base = Mock()
        mock_data_base.ingredients = value
        buns = Database.available_ingredients(mock_data_base)
        assert buns == value