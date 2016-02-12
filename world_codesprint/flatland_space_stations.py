cities, stations = [int(x) for x in input().strip().split(' ')]
station_cities = [int(c_temp) for c_temp in input().strip().split(' ')]

def find_max_dist(city_list):
    dist_list = []
    city_list.sort()
    for i in range(len(city_list)):
        try:
            dist_list.append(abs(city_list[i] - city_list[i+1]))
        except IndexError:
            pass

    first_city = abs(0 - city_list[0])
    last_city = abs(cities - (city_list[-1] + 1))
    return max(first_city, last_city, max(dist_list, default=0) // 2, 0)

print(find_max_dist(station_cities))
