weight = 41.5

# Ground shipping

if weight <= 2:
  cost = 1.5*weight + 20
  print("Cost: " + str(cost))
elif 2 < weight<= 6:
  cost = 3.00*weight + 20
  print("Cost: " + str(cost))
elif 6 < weight <= 10:
  cost = 4.00*weight + 20
  print("Cost: " + str(cost))
else:
  cost = 4.75*weight + 20
  print("Cost: " + str(cost)) 

# Premium Ground Shipping

premiumGroundShippingCost = 125
print(premiumGroundShippingCost)

# Drone Shipping

if weight <= 2:
  cost = 4.5*weight + 0.0
  print("Cost: " + str(cost))
elif 2 < weight<= 6:
  cost = 9.00*weight + 0.0
  print("Cost: " + str(cost))
elif 6 < weight <= 10:
  cost = 12.00*weight + 0.0
  print("Cost: " + str(cost))
else:
  cost = 14.25*weight + 0.0
  print("Cost: " + str(cost)) 