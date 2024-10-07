from abc import ABC, abstractmethod

# Gemeinsames Iterator-Interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Gemeinsames Interface für die Sammlung
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# Konkrete Sammlung: Musik-Playlist
class Playlist(IterableCollection):
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def create_iterator(self):
        return PlaylistIterator(self.songs)

# Konkreter Iterator: Playlist-Iterator, der das Python Iterator-Protokoll implementiert
class PlaylistIterator(Iterator):
    def __init__(self, songs):
        self.songs = songs
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < len(self.songs):
            song = self.songs[self.position]
            self.position += 1
            return song
        else:
            raise StopIteration

    def has_next(self):
        return self.position < len(self.songs)

    def next(self):
        return self.__next__()

# Verwendung des Iterator Patterns
if __name__ == "__main__":
    # Erstellen der Playlist
    playlist = Playlist()
    playlist.add_song("Song 1")
    playlist.add_song("Song 2")
    playlist.add_song("Song 3")

    # Songs in der Playlist mit einer for-Schleife durchlaufen
    for song in playlist.create_iterator():
        print(f"Abspiele: {song}")
