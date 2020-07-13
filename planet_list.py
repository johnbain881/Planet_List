planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
planet_list.append("Pluto")
rocky_planets = planet_list[:4]
del planet_list[-1]
print(rocky_planets)
print(planet_list)


spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]

for planet in planet_list:
  for my_tuple in spacecraft:
    if planet == my_tuple[1]:
      print(f"{my_tuple[0]} has visited {planet}")
