class FourPrimes:
    def __init__(self):
        self.run()

    
    def getPrimes(self, n):
        """
        Return a list of all prime numbers less than n

        :param n: Limite superior
        :type n: int
        :return: lista de primos
        :rtype: list
        """
        primes = [2]
        for i in range(3, n+1, 2):
            if i > n:
                break
            sqr = int(i ** 0.5)
            prime = True
            for j in range(3, sqr+1, 2):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                primes.append(i)
        return primes
    
    def get2Factors(self, n, primes, depth):
        """
        Return 2 factors of n, each of which is a prime number, using a recursive approach.
        If it is not possible to find two factors that are prime numbers, return False.
        
        :param n: The number to find the factors.
        :type n: int
        :param primes: A list of prime numbers.
        :type primes: list
        :param depth: The depth of the recursion.
        :type depth: int
        :return: A list of two factors of n, each of which is a prime number, or False.
        :rtype: list or bool
        """
        # stringDebug = ""
        # for i in range(depth):
        #     stringDebug += "    "
        if depth == 2:
            # print(f"{stringDebug}N = {n}")
            return n if n in primes else False
        a = n // 2
        b = n - a
        while b >= 2:
            # print(f"{stringDebug}A = {a}, B = {b}")
            resultA = self.get2Factors(a, primes, depth+1)
            resultB = self.get2Factors(b, primes, depth+1)
            if resultA and resultB:    
                return [resultA, resultB]
            a += 1
            b -= 1
        return False  
    def run(self):
        """
        Continuously reads integers from input and determines if they can be expressed as the sum of four prime numbers.
        
        If the input number is less than or equal to 7, it prints "Impossible" because a number less than 8 cannot
        be expressed as the sum of four prime numbers. For other numbers, it attempts to find four prime numbers whose
        sum equals the input number. If such numbers are found, they are printed; otherwise, "Impossible" is printed.
        
        The process continues until an exception occurs (e.g., non-integer input).
        """
        while True:
            try:
                n = int(input())
                #Impossivel escrever qualquer numero menor que 8 como a soma de 4 numeros primos (2 + 2 + 2 + 2 = 8)
                if n <= 7:
                    print("Impossible")
                    continue
                primes = self.getPrimes(n)
                result = self.get2Factors(n, primes, 0)
                if not result:
                    print("Impossible")
                else:
                    result = [x for sublist in result for x in sublist]
                    resposta = ""
                    for i in result:
                        resposta = resposta + f"{i} "
                    print(resposta)
            except:
                break