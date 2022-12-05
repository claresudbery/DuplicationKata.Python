from Song import Song


def get_next_prime(number):
    next = {13: 17, 17: 19, 19: 23, 23: 29}
    return next[number]

class Lesson3HigherOrderFunctions(Song):
    def sing_song(self):
        number = 2
        self.sing(str(number) + "! ")
        number = number + 2
        self.sing(str(number) + "! ")
        number = number + 2
        self.sing(str(number) + "! ")
        number = number + 2
        self.sing(str(number) + "! ")
        self.sing("Who do we appreciate?")
        number = 17
        self.sing(str(number) + "! ")
        number = get_next_prime(number)
        self.sing(str(number) + "! ")
        number = get_next_prime(number)
        self.sing(str(number) + "! ")
        number = get_next_prime(number)
        self.sing(str(number) + "! ")
        self.sing("These are the primes, that we find fine!")

