import random

from song import Song, Genre


class Playlist:
    '''
    Плейліст (Коллекція пісень)
    
    - Створити новий плейліст, додавши назву
    - Можливість додати пісню
    - Можливість йти по піснях

    '''
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.songs[key]
        return self.songs[key.start:key.stop:key.step]
        # return self.songs[key[0] /]
    
    def __iadd__(self, song: Song):
        self.add_song(song)
        return self
    
    def __iter__(self):
        '''Починає ітерацію'''
        return PlaylistIterator(self.songs)
    
    def create_shuffle_iterator(self):
        return PlaylistShuffleIterator(self.songs)

    # def __next__(self):
    #     '''Повертає. наступний елемент'''
    #     if self.iteration_index >= len(self.songs):
    #         raise StopIteration
    #     next_element = self.songs[self.iteration_index]
    #     self.iteration_index += 1
    #     return next_element
    
    def __call__(self):
        # sum is way better
        # total_seconds = 0
        # for song in self.songs:
        #     total_seconds += song.duration_in_seconds
        # return total_seconds
        # generator = (song.duration_in_seconds for song in self.songs)
        # print(generator)
        return sum(song.duration_in_seconds for song in self.songs)

    def __str__(self) -> str:
        return f'Playlist(name="{self.name}", songs={self.songs})'


class PlaylistIterator:
    def __init__(self, songs: list[Song]):
        self.iteration_index = 0
        self.songs = songs

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration_index >= len(self.songs):
            raise StopIteration
        next_element = self.songs[self.iteration_index]
        self.iteration_index += 1
        return next_element
    

class PlaylistShuffleIterator:
    def __init__(self, songs: list[Song]):
        self.iteration_index = 0
        songs_copy = songs[:]
        random.shuffle(songs_copy)
        self.songs = songs_copy

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration_index >= len(self.songs):
            raise StopIteration
        next_element = self.songs[self.iteration_index]
        self.iteration_index += 1
        return next_element

if __name__ == '__main__':
    song_one = Song("Author One", "Song One", 100, Genre.POP)
    song_two = Song("Author Two", "Song Two", 300, Genre.ROCK)

    playlist_one = Playlist("Playlist one")
    # playlist_one.add_song(song_one)
    # playlist_one.add_song(song_two)
    playlist_one += song_one
    # print(playlist_one)
    playlist_one += song_two

    print(playlist_one)

    # print(playlist_one())

    iterator = iter(playlist_one.create_shuffle_iterator())
    print(next(iterator))

    iterator_two = iter(playlist_one.create_shuffle_iterator())
    print(next(iterator_two))
    print(next(iterator_two))

    print(next(iterator))

    print(playlist_one)

    with open("hello.txt"):
        ...

    # for el in playlist_one:
    #     print(el)



    # playlist_one("John", "Doe")
    # my_list = [1, 2, 3]
    # print(my_list[::-1])
