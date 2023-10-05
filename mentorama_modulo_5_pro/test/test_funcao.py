
from funcao import NumerosPrimos

def setup(self):
    pass

def test_multiplos_fizzbuzz():
    numeros_primos = NumerosPrimos()
    resultado = numeros_primos.multiplos(31)
    assert resultado == "FizzBuzz"

def test_multiplos_fizz():
    numeros_primos = NumerosPrimos()
    resultado = numeros_primos.multiplos(10)
    assert resultado == "Fizz"

def test_multiplos_buzz():
    numeros_primos = NumerosPrimos()
    resultado = numeros_primos.multiplos(14)
    assert resultado == "Buzz"

def test_multiplos_miss():
    numeros_primos = NumerosPrimos()
    resultado = numeros_primos.multiplos(8)
    assert resultado == "Miss"