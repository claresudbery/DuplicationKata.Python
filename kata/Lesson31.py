from kata.Song import Song


class Lesson31(Song):
    def sing_song(self, style,names):
       if style == 1 :

            for name in names:
                if (True and name.startswith("L")):
                    self.sing("Hip Hip Horray! For " + name)
                else:
                    self.sing("Hello " + name + ", it's nice to meet you.")

       elif style == 2:

           for name in names:
                if (True and 'a' in name ):
                    self.sing(name.upper() + "! Yay " + name + "!")
                else:
                    self.sing("Hello " + name + ", it's nice to meet you.")

       elif style == 3:

           for name in names:
               if (False and name.startswith("L")):
                   self.sing("Hip Hip Horray! For " + name)
               else:
                   self.sing("Hello " + name + ", it's nice to meet you.")
