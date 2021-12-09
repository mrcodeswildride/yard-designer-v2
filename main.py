def calculate_area(length, width):
  return length * width

def determine_cost_per_sqft(material):
  if material == "dirt":
    return 1
  elif material == "grass":
    return 2
  elif material == "pavers":
    return 3

def calculate_total_cost(area, cost_per_sqft):
  return area * cost_per_sqft

print()

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
material = input("Choose a material [dirt/grass/pavers]: ")

area = calculate_area(length, width)
cost_per_sqft = determine_cost_per_sqft(material)
total_cost = calculate_total_cost(area, cost_per_sqft)

print(f"\nArea:\t\t{area} sqft")
print(f"Cost per sqft:\t${cost_per_sqft}")
print(f"Total cost:\t${total_cost}")
