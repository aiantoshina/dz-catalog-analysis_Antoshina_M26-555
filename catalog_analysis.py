import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", 
                                                    "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

#Этап 1
def average_rating(movies):
    """Возвращает среднюю оценку оценку по каталогу, округленную до одного знака."""
    return round(sum(m["rating"] for m in movies) / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (самый старый фильм, самый новый фильм, среднее)."""
    ages = [current_year - m["year"] for m in movies]
    oldest = max(ages)
    newest = min(ages)
    avg_age = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, avg_age)

def duration_in_hours(minutes):
    """Переводит минуты в формат 'Xч Yм'."""
    return f"{minutes // 60}ч {minutes % 60}м"

#Этап 2
def rating_tier(rating):
    """Возвращает категорию по оценке. Использует if/elif, тернарный оператор."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо" if rating < 5 else "неизвестно"

def decode_label(year):
    """Возвращает метку по году. Использует оператор match."""
    match year:
        case y if y > 2020:
            return "новые"
        case y if 2015 <= y <= 2020:
            return "недавние"
        case y if y < 2015:
            return "старые"
        case _:
            return "неизвестно"
        
#Этап 3
#Названия всех фильмов, которые НЕ относятся к жанру "comedy"
for m in movies:
    if "comedy" in m["genres"]:
        continue
    print(m["title"])

#Поиск первого по порядку в списке фильма с рейтингом выше 9.0
i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(f"Найден: {movies[i]['title']}")
        break
    i += 1
else:
    print("Шедевров не найдено")

#Количество фильмов длиннее threshold минут
def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее threshold минут. Использует for."""
    count = 0
    for m in movies:
        if m["duration_min"] > threshold:
            count += 1
    return count       

#Этап 4
def normalize_title(title):
    """Приводит строку к формату Title Case."""
    words = title.split()
    res = []
    for w in words:
        if w:
            res.append(w[0].upper() + w[1:])
    return " ".join(res)

def make_slug(title):
    """Превращает нормализованное название в «слаг» вида the-quiet-algorithm."""
    norm = normalize_title(title)
    return norm.lower().replace(" ", "-")

def format_report_line(movie):
    """Возвращает единую строку с описанием фильма."""
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) - {movie["rating"]}/10, '
        f'{duration}, жанры: {genres}'
    )

#Этап 5
def titles_sorted_by_rating(movies):
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in sorted_movies]
#Демонстрация работы функции
titles = titles_sorted_by_rating(movies)
for title in titles:
    print(title)

def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) — топ по рейтингу."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in sorted_movies[:n]]
#Демонстрация работы функции
top3 = top_n_by_rating(movies, 3)
print(top3)

#Этап 6
def count_by_genre(movies):
    """Считает количество фильмов по жанрам. Использует метод dict.get()."""
    counts = {}
    for m in movies:
        for g in m["genres"]:
            counts[g] = counts.get(g, 0) + 1
    return counts

def actor_filmography(movies):
    """Возвращает словарь {актер: [список названий фильмов]}."""
    filmography = {}
    for m in movies:
        for a in m["actors"]:
            if a not in filmography:
                filmography[a] = []
            filmography[a].append(m["title"])
    return filmography

def high_rated_dict(movies):
    """Возвращает словарь {title: rating} для фильмов с рейтингом выше среднего."""
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}

#Этап 7
def all_genres(movies):
    """Возвращает множество всех уникальных жанров каталога."""
    res = set()
    for m in movies:
        res.update(m["genres"])
    return res

def common_actors(movie1, movie2):
    """Возвращает множество актеров, снимавшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b."""
    genres_a = set()
    for m in movies_a:
        genres_a.update(m["genres"])
    genres_b = set()
    for m in movies_b:
        genres_b.update(m["genres"])
    return genres_a - genres_b

#Этап 8
def iter_high_rated(movies, min_rating=8.0):
    """Генератор, лениво отдающий фильмы с рейтингом >= min_rating."""
    for m in movies:
        if m["rating"] >= min_rating:
            yield m

#Демонстрация работы функции-генератора
for movie in iter_high_rated(movies):
    print(format_report_line(movie))

#Генераторное выражение, считает общую длительность фильмов с рейтингом > 7 в минутах
sum_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)
print(f"Суммарная длительность фильмов с рейтингом > 7: {sum_duration} мин.")

#Этап 9
def build_report(movies):
    """Объединяет результаты всех предыдущих этапов и выводит единый отчет."""
    print("ОТЧЕТ ПО КАТАЛОГУ\n")
    print(f"Средний рейтинг: {average_rating(movies)}\n")

    _, _, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет\n")
    print()

    print("Топ-3 фильма:")
    top3 = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]
    for m in top3:
        title = normalize_title(m["title"])
        duration = duration_in_hours(m["duration_min"])
        genres = ", ".join(sorted(m["genres"]))
        print(
            f'"{title}" ({m["year"]}) – {m["rating"]}/10, {duration}, жанры: {genres}'
            )
    print()

    print("Фильмов по жанрам:")
    counts = count_by_genre(movies)
    for g, c in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{g} - {c}")
    print()

    print(f"Все жанры каталога: {', '.join(sorted(all_genres(movies)))}")