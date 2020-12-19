import sys
from orbits import Orbit


# prints the desired output as 'VEHICLE ORBITNUMBER'
def print_output(sortedOrbitTime):
    output = list(sortedOrbitTime.keys())[0]
    vehicle = output[0]
    orbit = output[1]
    if orbit == 1:
        print(vehicle, 'ORBIT1')
    else:
        print(vehicle, 'ORBIT2')


if __name__ == '__main__':

    orbit = Orbit()
    # file = open('inputFile.txt', 'r+')
    file = open(sys.argv[1], 'r+')
    for inputString in file.readlines():

        weather = inputString.split()[0]
        orbit1Speed = int(inputString.split()[1])
        orbit2Speed = int(inputString.split()[2])
        orbit.change_in_crater(weather)
        sortedOrbitTime = orbit.calculate_time_required_for_orbits(
            weather, orbit1Speed, orbit2Speed)
        print_output(sortedOrbitTime)
        orbit = Orbit()
