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


if __name__ == '__main__':
    song_one = Song("Author One", "Song One", 100, Genre.POP)
    song_two = Song("Author Two", "Song Two", 300, Genre.ROCK)

    playlist_one = Playlist("Playlist one")
    # playlist_one.add_song(song_one)
    # playlist_one.add_song(song_two)
    playlist_one += song_one
    print(playlist_one)
    playlist_one += song_two

    print(playlist_one())

    # playlist_one("John", "Doe")
    # my_list = [1, 2, 3]
    # print(my_list[::-1])
