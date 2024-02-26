from kata.Song import Song


class Lesson31(Song):
    def sing_song(self, style,names):
       if style == 1 :
            name_check = lambda name1: name1.startswith("L")
            special_greeting = lambda name2: "Hip Hip Horray! For " + name2

            for name in names:
                if (name_check(name)):
                    self.sing(special_greeting(name))
                else:
                    self.sing("Hello " + name + ", it's nice to meet you.")

       elif style == 2:
           name_check = lambda name1: 'a' in name1
           special_greeting = lambda name2: name2.upper() + "! Yay " + name2 + "!"

           for name in names:
               if (name_check(name)):
                   self.sing(special_greeting(name))
               else:
                   self.sing("Hello " + name + ", it's nice to meet you.")

       elif style == 3:
           name_check = lambda name1: False
           special_greeting = lambda name2: "Hip Hip Horray! For " + name2

           for name in names:
               if (name_check(name)):
                   self.sing(special_greeting(name))
               else:
                   self.sing("Hello " + name + ", it's nice to meet you.")
