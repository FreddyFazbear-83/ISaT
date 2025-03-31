import json

with open('cat.json', 'r', encoding='utf-8') as file:
    books = json.load(file)

print("Сколько вам лет? ")
cat = int(input('Мне: '))

genres_under_12 = [
    "Фэнтези", "Приключения", "Детектив", "Романтика", "Юмор", "Детская литература", "Детская поэзия"
]

genres_12_and_above = [
    "Научная фантастика", "Ужасы", "Историческая проза", "Триллер",
    "Мемуары и автобиографии", "Философская литература", "Научно-популярная литература",
    "Поэзия", "Драма", "Сказки"
]

text1 = "Тихий и стандартный совет - 'Тихий Дэн'"

selected_author = None
selected_genre = None
recommended_books = []

# Исправлено условие для проверки возраста
if cat <= 12:
    print("Какой жанр бы вы хотели прочесть? (доступные жанры для вашего возраста)")
    for index, genre in enumerate(genres_under_12, start=1):
        print(f"{index}. {genre}")
    genre_choice = int(input('Выберите номер жанра: '))

    if 1 <= genre_choice <= len(genres_under_12):
        selected_genre = genres_under_12[genre_choice - 1]
    else:
        print("Ошибка: введён неверный номер жанра.")

elif cat > 12:
    print("Какой жанр бы вы хотели прочесть? (доступные жанры для вашего возраста)")
    for index, genre in enumerate(genres_12_and_above, start=1):
        print(f"{index}. {genre}")
    genre_choice = int(input('Выберите номер жанра: '))

    if 1 <= genre_choice <= len(genres_12_and_above):
        selected_genre = genres_12_and_above[genre_choice - 1]
    else:
        print("Ошибка: введён неверный номер жанра.")
        print(text1)

available_authors = [author for author in books if selected_genre in books[author]]

if available_authors:
    print("Хотите выбрать автора книг? (можно написать только 'да')")
    want_author = input().strip().lower()

    if want_author == 'да':
        print("Вот список авторов, у которых есть книги в жанре '{}':".format(selected_genre))
        for index, author in enumerate(available_authors, start=1):
            print(f"{index}. {author}")

        author_choice = int(input("Выберите номер автора (или введите 0, чтобы пропустить): "))

        if author_choice == 0:
            print("Вы пропустили выбор автора.")
        elif 1 <= author_choice <= len(available_authors):
            selected_author = available_authors[author_choice - 1]
        else:
            print(text1)
else:
    print(f"Извините, для выбранного жанра '{selected_genre}' нет доступных авторов.")

if selected_author and selected_genre:
    if selected_author in books and selected_genre in books[selected_author]:
        cat_limit = books[selected_author][selected_genre]["возрастное ограничение"]
        if cat >= cat_limit:
            recommended_books = books[selected_author][selected_genre]["книги"]
        else:
            print(f"Извините, для вашего возраста (от {cat}) нет доступных книг в жанре '{selected_genre}' от автора '{selected_author}'.")
else:
    print("Ошибка: не выбран автор или жанр.")

if recommended_books:
    print("Рекомендуемые книги:")
    for book in recommended_books:
        print(f"- {book}")
else:
    print('Извините, для выбранного автора и жанра нет рекомендаций.')
    print(text1)