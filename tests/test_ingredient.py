class TestIngredient:

    def test_get_price_ingredient(self, ingredient):
        ingredient.get_price()
        assert ingredient.price == 90

    def test_get_name_ingredient(self, ingredient):
        ingredient.get_name()
        assert ingredient.name == 'Соус Spicy-X'

    def test_get_type_ingredient(self, ingredient):
        ingredient.get_type()
        assert ingredient.type == 'SAUCE'
