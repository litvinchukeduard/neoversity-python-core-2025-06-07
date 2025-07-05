from song import Song


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

    def __str__(self) -> str:
        return f'Playlist(name="{self.name}", songs={self.songs})'


if __name__ == '__main__':
    playlist_one = Playlist("Playlist one")
    print(playlist_one)
