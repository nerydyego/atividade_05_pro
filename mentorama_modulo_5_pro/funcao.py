"""
Função de numeros multiplos de 5 e 7
"""
class NumerosPrimos:
    def multiplos(self, var1):    
        """ Verifica se um número é múltiplo de 5 e/ou 7. 
    Args: 
        var1 (int): O número a ser verificado.
    Returns:
        str: 'FizzBuzz' se var1 for múltiplo de ambos 5 e 7.
             'Fizz' se var1 for múltiplo de 5.
             'Buzz' se var1 for múltiplo de 7.
             'Miss' caso contrário.
        """
        if var1 % 5 == 0 and var1 % 7 == 0:
            return 'FizzBuzz'
        if var1 % 5 == 0:
            return "Fizz"
        if var1 % 7 == 0:
            return "Buzz"
        return "Miss"