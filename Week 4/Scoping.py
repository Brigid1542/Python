greek = "alpha"
print("Global declaration: "+greek, id(greek))
def b():
    greek="beta"
    print("Inside local: "+greek, id(greek))
def c():
    greek="gamma"
    print("Enclosed: "+greek, id(greek))
c()
print("Inside local:End of local scope: "+greek, id(greek))
b()
print("Global after local execution: "+greek, id(greek))
