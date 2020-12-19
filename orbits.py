from vehicles import Vehicle

# decrease in crater as per weather
DECREASE_SUNNY = 10
DECREASE_RAINY = -20

# Orbit distance in megamiles
ORBIT1_DISTANCE = 18
ORBIT2_DISTANCE = 20

# no of craters in orbits
ORBIT1_CRATER = 20
ORBIT2_CRATER = 10


class Orbit:
    # each atribute is an orbit used by vehicles to travel
    # initializes every attribute with orbit_distance and no_of_crater in it
    def __init__(self):
        self.orbit1 = [ORBIT1_DISTANCE, ORBIT1_CRATER]
        self.orbit2 = [ORBIT2_DISTANCE, ORBIT2_CRATER]

    # decrease/increase  the pecentage of crater
    def percentage_change_in_crater(self, percentChange):
        actualChange = (self.orbit1[1] * percentChange) / 100
        self.orbit1[1] -= actualChange
        actualChange = (self.orbit2[1] * percentChange) / 100
        self.orbit2[1] -= actualChange

    # depending upon the weather, changes crater in each orbit
    def change_in_crater(self, weather):
        if weather == 'SUNNY':
            self.percentage_change_in_crater(DECREASE_SUNNY)
        elif weather == 'RAINY':
            self.percentage_change_in_crater(DECREASE_RAINY)

    # returns the sorted final time to travel by each vehicle in each orbit
    def sort_time(self, orbitTime):
        sorted_times = sorted(orbitTime, key=orbitTime.get)
        sorted_orbitTime = {}
        for key in sorted_times:
            sorted_orbitTime[key] = orbitTime[key]

        return sorted_orbitTime

    # calculates total time required by each vehicle to travel each orbit
    # returns the result as dictionary
    def calculate_time_required_for_orbits(self, weather, orbit1Speed,
                                           orbit2Speed):
        vehicle = Vehicle()
        vehicle.can_vehicle_travel(weather)
        vehicle.update_vehicle_speed(orbit1Speed)
        orbitNumber = 1
        orbit1Time = vehicle.calculate_time_required_to_travel(
            self.orbit1, orbitNumber)

        vehicle = Vehicle()
        vehicle.can_vehicle_travel(weather)
        vehicle.update_vehicle_speed(orbit2Speed)
        orbitNumber = 2
        orbit2Time = vehicle.calculate_time_required_to_travel(
            self.orbit2, orbitNumber)

        # merging two dictionaries to get a single dictionary of orbitTime
        orbit1Time.update(orbit2Time)

        # sorting values of time taken by vehicle to travel orbit
        sortedOrbitTime = self.sort_time(orbit1Time)

        return sortedOrbitTime
