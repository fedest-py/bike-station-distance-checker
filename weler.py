#******************************************************************************
# weler.py
#******************************************************************************
#Eduardo E
#

#ask user for latitude, longitude, and amount of bikes in station 1

latitude1 = float(input('Enter latitude of station 1: '))
longitude1 = float(input('Enter longitude of station 1: '))
bikes1 = float(input('Bikes at station 1: '))

#ask for the values for station 2

latitude2 = float(input('Enter latitude of station 2: '))
longitude2 = float(input('Enter longitude of station 2: '))
bikes2 = float(input('Bikes at station 2: '))

#calculate the changes in latitude and longitude for stations 1 and 2

change_in_latitude1 = 40.740230 - latitude1
change_in_longitude1 = -73.983766 - longitude1

change_in_latitude2 = 40.740230 - latitude2
change_in_longitude2 = -73.983766 - longitude2

#convert to kilometers

change_in_latitude1 = change_in_latitude1 * 111.048
change_in_longitude1 = change_in_longitude1 * 84.515

change_in_latitude2 = change_in_latitude2 * 111.048
change_in_longitude2 = change_in_longitude2 * 84.515

#calculate distance

import math

distance1 = math.sqrt((change_in_latitude1)**2 + (change_in_longitude1)**2)

distance2 =math.sqrt((change_in_latitude2)**2 + (change_in_longitude2)**2)

print(f'Distance to station 1 = {distance1}')
print(f'Distance to station 2 = {distance2} ')



#create a variable for the availability of bikes

bikes_available1 = False
bikes_available2= False
distance1_req = False
distance2_req = False


if bikes1 > 0:
    bikes_available1 = True

if bikes2 > 0:
    bikes_available2 = True

if distance1 < distance2 and distance1 < 3:
    distance1_req = True
    
if distance2 < distance1 and distance2 < 3:
    distance2_req = True


#decide which station is the most convenient


if distance1_req:
    if bikes_available1:
        print('Station 1')
    elif distance2 < 3 and bikes_available2:
        print('Station 2')
elif distance2_req:
    if bikes_available2:
        print('Station2')
    elif distance1 < 3 and bikes_available1:
        print('Station1')
else:
    print('Neither')



