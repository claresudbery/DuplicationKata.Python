from kata.Song import Song


class Lesson21(Song):
    def sing_song(self, style,names):
       if style == 1 :
            for name in names:
                if (name.startswith("L", 0)):
                    self.sing("Hip Hip Horray! For " + name)
                else:
                    self.sing("Hello " + name + ", it's nice to meet you.")
       elif style == 2:
           for name in names:
                if (name.startswith("am", 1)):
                    self.sing("Say yeah! Say yo! Say " + name)
                else:
                    self.sing("Hello " + name + ", it's nice to meet you.")
       elif style == 3:
           for name in names:
                self.sing("Hello " + name + ", it's nice to meet you.")
