from dataclasses import dataclass


@dataclass
class Song:
    '''
    Потрібно зберігати інформацію про пісню (автор, назва, довжина (сек), жанр)
    '''
    author: str
    title: str
    duration_in_seconds: int
    genre: str

# class Song:
#     '''
#     Потрібно зберігати інформацію про пісню (автор, назва, довжина (сек), жанр)
#     '''
#     def __init__(self, author: str, title: str, duration_in_seconds: int, genre: str):
#         self.author = author
#         self.title = title
#         self.duration_in_seconds = duration_in_seconds
#         self.genre = genre

#     def __str__(self):
#         return f'Song(author={self.author}, {self.title}, {self.duration_in_seconds}, {self.genre})'
        

if __name__ == '__main__':
    song = Song("Author One", "Song One", 300, "Pop")
    # print(song.title)
    print(song)
