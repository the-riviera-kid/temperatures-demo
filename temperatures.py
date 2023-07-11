class Kelvin():
    def __init__(self, temp: int) -> None: 
        self._temp = temp

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Kelvin) or isinstance(other, Celcius):
            other_as_kelvin = other.to_kelvin()
            return self._temp == other_as_kelvin._temp
        else:
            raise NotImplementedError()
            
    def __add__(self, other: "Kelvin") -> "Kelvin":
        return Kelvin(self._temp + other._temp)
    
    def __floordiv__(self, divisor: int) -> "Kelvin":
        return Kelvin(self._temp // divisor)
    
    def to_kelvin(self) -> "Kelvin":
        return self
     
class Celcius():
    def __init__(self, temp: int) -> None:
        self._temperature = temp

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Celcius) or isinstance(other, Kelvin):
            self_in_kelvin = self.to_kelvin()
            other_in_kelvin = other.to_kelvin()
            return self_in_kelvin == other_in_kelvin
        else:
            raise NotImplementedError()
    
    def to_kelvin(self) -> Kelvin:
        return Kelvin(self._temperature + 273)