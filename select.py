import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:password@localhost:5432/postgres')

connect = engine.connect()


album_2018 = connect.execute("""SELECT name, year_of_issue From album
WHERE year_of_issue = 2018;
""").fetchall()
print('Альбомы, вышедшие в 2018 году:', album_2018)

max_track = connect.execute("""SELECT name, duration FROM track 
WHERE duration = (SELECT MAX(duration) FROM track );
""").fetchall()
print('Самый длительный трек:', max_track)

tracks3 = connect.execute("""SELECT name FROM track 
WHERE duration >= 3
ORDER BY duration;
""").fetchall()
print('Треки длиннее 3 минут:', tracks3)

collection_year = connect.execute("""SELECT name FROM collection 
WHERE year_of_issue BETWEEN 2018 AND 2020;
""").fetchall()
print('Сборники, вышедшие в период с 2018 по 2020 год:', collection_year)

performer_1word = connect.execute("""SELECT name FROM performer 
WHERE LENGTH(TRIM(name))-LENGTH(REPLACE(TRIM(name), ' ', ''))=0;
""").fetchall()
print('Исполнители, чье имя состоит из 1 слова', performer_1word)

track_with_my = connect.execute("""SELECT name FROM track 
WHERE  name ILIKE '%%мой%%' OR name ILIKE '%%my%%';
""").fetchall()
print('Название треков, которые содержат слово "мой"/"my":', track_with_my)
