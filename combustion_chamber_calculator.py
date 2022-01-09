import math

'''
Turbocharger jet engine combustion chamber specifications calculator.
Specifications taken from paper titled: Turbocharger Jet Engine Build and Engineering Analysis
    by Han Ju Lee, Nick Strahan, Emily Boyd (https://openscholarship.wustl.edu/mems500/13/)
Code author: Ben Michaels

'''
#turbocharger specs
inletDiameter = 61.5     #mm
inletRadius = inletDiameter / 2     #mm
inletArea = math.pi * pow(inletRadius, 2)   #mm^2

print("inlet diameter:", inletDiameter, "mm")
print("inlet radius:", inletRadius, "mm")
print("inducer area:", inletArea, "mm^2")
print()

#primary holes
primaryHolesTotalArea = inletArea * .3      #mm^2
areaOfOnePrimaryHole = primaryHolesTotalArea / 24 #mm^2
radiusOfOnePrimaryHole = math.sqrt(areaOfOnePrimaryHole / math.pi) #mm^2

print("Total area of summation of primary holes:", primaryHolesTotalArea, "mm^2")
print("Number of primary holes:", 24)
print("Area of one primary hole:", areaOfOnePrimaryHole, "mm^2")
print("Radius of one primary hole:", radiusOfOnePrimaryHole, "mm")
print()

#secondary holes
secondaryHolesTotalArea = inletArea * .2 #mm^2
areaOfOneSecondaryHole = secondaryHolesTotalArea / 8 #mm^2
radiusOfOneSecondaryHole = math.sqrt(areaOfOneSecondaryHole / math.pi)  #mm^2

print("Total area of summation of secondary holes:", secondaryHolesTotalArea, "mm^2")
print("Number of secondary holes:", 8)
print("Area of one secondary hole:", areaOfOneSecondaryHole, "mm^2")
print("Radius of one secondary hole:", radiusOfOneSecondaryHole, "mm")
print()

#tertiary holes
tertiaryHolesTotalArea = inletArea * .5 #mm^2
areaOfOneTertiaryHole = tertiaryHolesTotalArea / 8 #mm^2
radiusOfOneTertiaryHole = math.sqrt(areaOfOneTertiaryHole / math.pi) #mm^2

print("Total area of summation of tertiary holes:", tertiaryHolesTotalArea, "mm^2")
print("Number of tertiary holes:", 8)
print("Area of one tertiary hole:", areaOfOneTertiaryHole, "mm^2")
print("Radius of one tertiary hole:", radiusOfOneTertiaryHole, "mm")
print()

#combustion chamber
lengthCombustionChamber = 6 * inletDiameter #mm
diameterInnerLiner = 2 * inletDiameter #mm
gapBetweenInnerAndOuterLiner = inletDiameter / 2 #mm

print("Length of Outer Casing: ", lengthCombustionChamber, "mm")
print("Diameter of Outer Casing: ", diameterInnerLiner + gapBetweenInnerAndOuterLiner, "mm")
print("Length of Inner Liner: ", lengthCombustionChamber * .95, "mm") #paper doesn't describe inner length, but is 95% of chamber length
print("Diameter of Inner Liner: ", diameterInnerLiner, "mm")
print("Gap between inner liner and outer casing: ", gapBetweenInnerAndOuterLiner, "mm")
print()
