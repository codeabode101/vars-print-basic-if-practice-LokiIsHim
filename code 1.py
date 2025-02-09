name= input("what is your name")
fuel_level=100
starting_planet="saturn"
print(f"{name} blasts off from {starting_planet}")
if fuel_level==100:
    print("Fuel tank is full! Ready for launch!")
else: 
    print("Fill the rocket") 
new_planet="earth"
print(f"ALERT! Approaching {new_planet}!")
if new_planet=="earth":
    print("You see craters!")
else: 
    print("You see clouds!") 
if fuel_level>=50:
    print("Fuel level is good for landing.")
else: 
    print("Warning: Low fuel for landing!") 
