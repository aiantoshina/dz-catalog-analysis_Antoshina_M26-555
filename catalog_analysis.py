movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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

import math

#Этап 1
def average_rating(movies):
    """Возвращает среднюю оценку оценку по каталогу, округленную до одного знака."""
    return round(sum(m["rating"] for m in movies) / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее)."""
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
print("--- Не комедии ---")
for m in movies:
    if "comedy" in m["genres"]:
        continue
    print(m["title"])

#Поиск первого по порядку в списке фильма с рейтингом выше 9.0
print("--- Поиск первого фильма с рейтингом > 9.0 ---")
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
    return f'"{title}" ({movie["year"]}) - {movie["rating"]}/10, {duration}, жанры: {genres}'