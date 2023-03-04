<<<<<<< HEAD
def liters_100km_to_miles_gallon(liters):
    miles_100k = 100 / (1609.344 / 1000 )
    galons = liters / 3.785411784
    
    mpg = miles_100k / galons
    
    return mpg
    

def miles_gallon_to_liters_100km(miles):
    #recibo miles recorridas con un galon
    liters = 3.785411784 
    distanciaKm = miles * (1609.344 / 1000 )#Distancia recorrida en kilometros
    kml = distanciaKm/liters
    litrosEn100km = 100 / kml
    
    return litrosEn100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
=======
def liters_100km_to_miles_gallon(liters):
    miles_100k = 100 / (1609.344 / 1000 )
    galons = liters / 3.785411784
    
    mpg = miles_100k / galons
    
    return mpg
    

def miles_gallon_to_liters_100km(miles):
    #recibo miles recorridas con un galon
    liters = 3.785411784 
    distanciaKm = miles * (1609.344 / 1000 )#Distancia recorrida en kilometros
    kml = distanciaKm/liters
    litrosEn100km = 100 / kml
    
    return litrosEn100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
>>>>>>> dfd5fcc97c4e4339a5e4684ceb9fc1247b7c2ddc
