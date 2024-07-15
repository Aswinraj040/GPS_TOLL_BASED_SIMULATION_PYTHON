#Distance_calculation.py

from geopy.distance import geodesic

# Uses geopy to calculate the distance between two points
def calculate_distance(point1, point2):
    return geodesic((point1[1], point1[0]), (point2[1], point2[0])).kilometers