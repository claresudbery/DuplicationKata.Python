from kata.Song import Song


class Lesson31(Song):
    def sing_song(self, style, names):
        if style == 1:
            self.sing_cheers(
                names,
                lambda name1: name1.startswith("L"),
                lambda name2: "Hip Hip Horray! For " + name2
            )

        elif style == 2:
            self.sing_cheers(
                names,
                lambda name1: 'a' in name1,
                lambda name2: name2.upper() + "! Yay " + name2 + "!"
            )

        elif style == 3:
            self.sing_cheers(
                names,
                lambda name1: False,
                lambda name2: "Hip Hip Horray! For " + name2
            )

    def sing_cheers(self, names, name_check, special_greeting):
        for name in names:
            if (name_check(name)):
                self.sing(special_greeting(name))
            else:
                self.sing("Hello " + name + ", it's nice to meet you.")
