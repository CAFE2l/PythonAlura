from abc import ABC # abstract base classes
from numbers import complex 
from collections.abc import MutableSequence

class Playlist(MutableSequence):
    def __getitem__(self, item):
        super().__getitem__()


filmes = Playlist()
