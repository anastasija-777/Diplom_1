import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from data import Data


@pytest.fixture(scope='function')
def bun():
    return Bun(Data.NAME,Data.PRICE)

@pytest.fixture(scope='function')
def ingredient():
    return Ingredient(*Data.INGREDIENT)

@pytest.fixture(scope='function')
def burger():
    return Burger()

