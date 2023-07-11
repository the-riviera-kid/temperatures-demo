from temperatures import Kelvin, Celcius
def test_kelvin_exists() -> None:
    assert Kelvin(0)

def test_comparing_kelvin() -> None:
    assert Kelvin(3) == Kelvin(3)

def test_comparing_kelvin_that_do_not_match() -> None:
    assert not Kelvin(3) == Kelvin(8)

def test_adding_kelvin() -> None:
    assert Kelvin(3) + Kelvin(4) == Kelvin(7)

def test_dividing_kelvin() -> None:
    assert Kelvin(20) // 4 == Kelvin(5)

def test_celcius_exists() -> None:
    assert Celcius(23)

def test_comparing_celcius() -> None:
    assert Celcius(25) == Celcius(25)

def test_comparing_celcius_to_kelvin() -> None:
    assert Celcius(0) == Kelvin(273)

def test_comparing_kelvin_to_celcius() -> None:
    assert Kelvin(283) == Celcius(10)