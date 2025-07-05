from dataclasses import dataclass
from enum import StrEnum, Enum, auto

# GENRES = ["Pop", "Rock", "Metal",]
# Enum -> enumerate


class Genre(StrEnum):
    ROCK = auto()
    POP = auto()
    METAL = auto()


@dataclass
class Song:
    '''
    Потрібно зберігати інформацію про пісню (автор, назва, довжина (сек), жанр)
    '''
    author: str
    title: str
    duration_in_seconds: int
    genre: Genre

    # self.author, self.title
    def __post_init__(self):
        if self.duration_in_seconds < 0:
            raise ValueError("Duration can not be less than 0")
        # self.genre = self.genre.capitalize() # hello -> Hello


# class Song:
#     '''
#     Потрібно зберігати інформацію про пісню (автор, назва, довжина (сек), жанр)
#     '''
#     def __init__(self, author: str, title: str, duration_in_seconds: int, genre: str):
#         self.author = author
#         self.title = title
#         if duration_in_seconds < 0:
#             raise ValueError("Duration can not be less than 0")
#         self.duration_in_seconds = duration_in_seconds
#         self.genre = genre

#     def __str__(self):
#         return f'Song(author={self.author}, {self.title}, {self.duration_in_seconds}, {self.genre})'
        

if __name__ == '__main__':
    # {"author": "Author One"}
    song = Song("Author One", "Song One", 0, Genre.POP)
    song = Song("Author One", "Song One", 0, Genre.ROCK)

    # print("Choose genre: Pop - 1, Rock - 2")

    # song.genre = "Rock 10"
    # print(song.title)
    # print(song)
    print(Genre.POP.value)
