from kata.Song import Song


class Lesson31(Song):
    def sing_song(self, style,names):
       if style == 1 :

            for name in names:
                name_check = name.startswith("L")
                if (True and name_check):
                    self.sing("Hip Hip Horray! For " + name)
                else:
                    self.sing("Hello " + name + ", it's nice to meet you.")

       elif style == 2:

           for name in names:
                name_check = 'a' in name
                if (True and name_check):
                    self.sing(name.upper() + "! Yay " + name + "!")
                else:
                    self.sing("Hello " + name + ", it's nice to meet you.")

       elif style == 3:

           for name in names:
               name_check = name.startswith("L")
               if (False and name_check):
                   self.sing("Hip Hip Horray! For " + name)
               else:
                   self.sing("Hello " + name + ", it's nice to meet you.")
