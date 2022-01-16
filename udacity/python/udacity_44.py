# Testing boolean

altitude = 10000
speed = 250
propulsion = "Propeller"

# Validate TRUE or FALSE

result = altitude < 1000 and speed > 100
print(result) #-> Is False

result = (propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000
print(result) #-> Is False
    
result = not (speed > 400 and propulsion == "Propeller")
print(result) #-> Is true

result = (altitude > 500 and speed > 100) or not propulsion == "Propeller"
print(result) #-> Is True