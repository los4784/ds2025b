def duplicate_city(city):
    result = list()
    s = set()

    for cityin in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2: # 중복값이 들어옴
            result.append(city)
    return result

cities = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
# cities = {'Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul'}
cities = set(cities)
cities.append('Anyang')
cities.append('Seoul')
print(cities)
print(set(duplicate_city(cities)))