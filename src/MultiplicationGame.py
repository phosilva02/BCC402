class MultiplicationGame:
    def __init__(self):
        self.run()

    def run(self):
        while True:
            try:
                n = int(input())
                p = 1
                turn = 0
                mult = 2
                values = sorted(list(range(2, 10)), reverse=True)
                while (p * 9) < n:
                    for div in values:
                        if n / (p * div) <= 9:
                            if div == 2:
                                mult = 2
                            continue
                        mult = div
                        break
                    p *= mult
                    turn += 1
                if turn % 2:
                    print("Ollie wins.")
                else:
                    print("Stan wins.")
            except:
                break