import sys

sys.path.append('C:\\Users\\cordobda\\OneDrive - Micro Focus\\Documents\\Personal\\python\\Practicas\\modules')

from module import suml, prodl

print(__name__)
#print(module.__counter)



zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(zeroes)
print(ones)
print(suml(zeroes))
print(prodl(ones))




#prints the path where python looks for module files
for p in sys.path:
    print(p)

