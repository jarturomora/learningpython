# -*- coding: utf-8 -*-

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there\n"])

bulls_on_parade = Song(["They rally around the family",
                    "With pockets full of shells\n" ])

el_chorrito = Song(["Allá en la fuente",
                "Había un chorrito",
                "Se hacía grandote",
                "Se hacía chiquito",
                "Estaba de mal humor",
                "Pobre chorrito tenía calor\n"])

rola = ["Las piedras rodando se encuentran",
        "Y tu y yo algún día nos habremos de encontrar",
        "Mientras tanto cuídate",
        "Y que te bendiga Dios",
        "No hagas nada malo que no hiciera yo\n"]

una_del_tri = Song(rola)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

el_chorrito.sing_me_a_song()

una_del_tri.sing_me_a_song()