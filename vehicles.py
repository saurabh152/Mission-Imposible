# constants for speed, in megamiles/hour
CAR_SPEED = 20
BIKE_SPEED = 10
TUKTUK_SPEED = 12

# constants for time, to cross each crater in minutes
CAR_CRATER_TIME = 3
BIKE_CRATER_TIME = 2
TUKTUK_CRATER_TIME = 1

# weather in which vehicle can travel
CAR_WEATHER = ['RAINY', 'SUNNY', 'WINDY']
BIKE_WEATHER = ['SUNNY', 'WINDY']
TUKTUK_WEATHER = ['SUNNY', 'RAINY']


class Vehicle:
    # each atribute is a vehicle used to travel orbit
    # initializes every attribute with speed, craterTime,and canTravelInWeather
    def __init__(self):
        self.car = [CAR_SPEED, CAR_CRATER_TIME, True]
        self.bike = [BIKE_SPEED, BIKE_CRATER_TIME, True]
        self.tuktuk = [TUKTUK_SPEED, TUKTUK_CRATER_TIME, True]

    # checks if vehicle can travel in the given weather and updates the value
    def can_vehicle_travel(self, weather):
        if weather not in CAR_WEATHER:
            self.car[2] = False

        if weather not in BIKE_WEATHER:
            self.bike[2] = False

        if weather not in TUKTUK_WEATHER:
            self.tuktuk[2] = False

    # updates the speed of Vehicles according to orbitTrafficSpeed
    def update_vehicle_speed(self, orbitTrafficSpeed):
        if (int(orbitTrafficSpeed) <= CAR_SPEED):
            self.car[0] = orbitTrafficSpeed

        if (int(orbitTrafficSpeed) <= BIKE_SPEED):
            self.bike[0] = orbitTrafficSpeed

        if (int(orbitTrafficSpeed) <= TUKTUK_SPEED):
            self.tuktuk[0] = orbitTrafficSpeed

    # calculates time to cover the obit distance in hours
    def time_to_cover_orbit(self, orbitDistance, vehicleSpeed):
        return (orbitDistance / vehicleSpeed)

    # calculates time to cover crater in orbit
    def time_to_cover_crater(self, orbitCrater, vehicleTime):
        return ((orbitCrater * vehicleTime) / 60)

    # calculate total time required by every vehicle to travel
    # only if vehicle can travel in given weather
    def calculate_time_required_to_travel(self, orbitData, orbitNumber):
        totalTime = {}
        if self.car[2]:
            carTimeOrbit = float(
                self.time_to_cover_orbit(orbitData[0], self.car[0]))
            carTimeCrater = float(
                self.time_to_cover_crater(orbitData[1], self.car[1]))
            totalCarTime = carTimeOrbit + carTimeCrater
            totalTime['CAR', orbitNumber] = totalCarTime

        if self.bike[2]:
            bikeTimeOrbit = float(
                self.time_to_cover_orbit(orbitData[0], self.bike[0]))
            bikeTimeCrater = float(
                self.time_to_cover_crater(orbitData[1], self.bike[1]))
            totalBikeTime = bikeTimeOrbit + bikeTimeCrater
            totalTime['BIKE', orbitNumber] = totalBikeTime

        if self.tuktuk[2]:
            tuktukTimeOrbit = float(
                self.time_to_cover_orbit(orbitData[0], self.tuktuk[0]))
            tuktukTimeCrater = float(
                self.time_to_cover_crater(orbitData[1], self.tuktuk[1]))
            totalTuktukTime = tuktukTimeOrbit + tuktukTimeCrater
            totalTime['TUKTUK', orbitNumber] = totalTuktukTime

        return totalTime
