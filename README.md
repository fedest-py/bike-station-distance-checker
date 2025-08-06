# bike-station-distance-checker


This Python program simulates a decision system for a bike-sharing company called Weler. Based on user input, it recommends which of two stations a rider should use.

## How it works:
1. Takes latitude, longitude, and bike availability for two bike stations.
2. Computes the distance between each station and the Weler HQ (flat-earth approximation).
3. Recommends:
   - The closest station within 3 km that has bikes.
   - "Neither" if no station is suitable.

##  Distance Formula:
Δx = (latitude difference) * 111.048
Δy = (longitude difference) * 84.515
Distance = √(Δx² + Δy²)


##  Example:
- Enter latitude of station 1: 40.75
- Enter longitude of station 1: -73.98
- Bikes at station 1: 5
- Enter latitude of station 2: 40.742
- Enter longitude of station 2: -73.983
- Bikes at station 2: 1

- Distance to station 1 = 1.13
- Distance to station 2 = 0.21

- Station 2

## 🧠 Concepts Demonstrated:
- Coordinate math and conversion to kilometers
- Conditionals and logic chaining
- Real-world modeling (bike-sharing decisions)
