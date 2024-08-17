#user input 
distance_km = float(input(" distance between the two cities in kilometer:"))

# Converion
distance_m = distance_km * 1000

distance_feet = distance_km * 3280.84

distance_inches = distance_km * 39370.1

distance_cm = distance_km * 100000

# Print the converted distances
print("Distance in meters:", distance_m)
print("Distance in feet:", distance_feet)
print("Distance in inches:", distance_inches)
print("Distance in centimeters:", distance_cm)
