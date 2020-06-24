# creating instances from data

cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = zip(cityNames, populations, states)
print(city_tuples)
class City:
    def __init__(self, n, p, s):
        self.name = n
        self.population = p
        self.state = s
    def __str__(self):
        return '{}, {} (pop: {})'.format(self.name, self.state, self.population)


#cities = []
#for city_tup in city_tuples:
#    name, pop, state = city_tup
#    city = City(name, pop, state) # instance of the city class
#    cities.append(city)


cities = [City(n, p, s) for (n, p, s) in city_tuples]
print(cities)
