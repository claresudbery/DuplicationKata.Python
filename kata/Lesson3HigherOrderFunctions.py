from kata.Song import Song


def get_next_prime(number):
    next = {13: 17, 17: 19, 19: 23, 23: 29}
    return next[number]


class Lesson3HigherOrderFunctions(Song):
    def sing_song(self):
        number = 2
        number_expression = number + 2
        solo_line = "Who do we appreciate?"

        self.sing_lines(number, number_expression, solo_line)

        number = 17
        number_expression = get_next_prime(number)
        solo_line = "These are the primes, that we find fine!"

        self.sing_lines(number, number_expression, solo_line)

    def sing_lines(self, number, number_expression, solo_line):
        repeated_line = str(number) + "! "
        self.sing(repeated_line)
        number = number_expression
        self.sing(repeated_line)
        number = number_expression
        self.sing(repeated_line)
        number = number_expression
        self.sing(repeated_line)
        self.sing(solo_line)
