import pytest
from praktikum.bun import Bun
from data import Data


class TestBun:

    @pytest.mark.parametrize('name',[None,'', 'Флюоресцентная булка R2-D3'])
    def test_get_name_bun(self,bun,name):
        bun = Bun(name,Data.PRICE)
        result = bun.get_name()
        assert result == name

    @pytest.mark.parametrize('price', [None, '', 988])
    def test_get_price_bun(self,bun,price):
        bun = Bun(Data.NAME, price)
        result = bun.get_price()
        assert result == price



