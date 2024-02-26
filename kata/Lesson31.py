from kata.Song import Song


class Lesson31(Song):
    def sing_song(self, style,names):
       if style == 1 :
            name_check = lambda name1: name1.startswith("L")

            for name in names:
                if (True and name_check(name)):
                    self.sing("Hip Hip Horray! For " + name)
                else:
                    self.sing("Hello " + name + ", it's nice to meet you.")

       elif style == 2:
           name_check = lambda name1: 'a' in name1

           for name in names:
               if (True and name_check(name)):
                   self.sing(name.upper() + "! Yay " + name + "!")
               else:
                   self.sing("Hello " + name + ", it's nice to meet you.")

       elif style == 3:
           name_check = lambda name1: name1.startswith("L")

           for name in names:
               if (False and name_check(name)):
                   self.sing("Hip Hip Horray! For " + name)
               else:
                   self.sing("Hello " + name + ", it's nice to meet you.")
