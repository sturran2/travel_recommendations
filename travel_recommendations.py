destinations=["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler=["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

#define function called get destination index

def get_destination_index(destination):
  destination_index =destinations.index(destination)
  return destination_index

#test function:
#print(get_destination_index("Chicago, IL"))

#define function to see where traveler is

def get_traveler_location(traveler):
  traveler_destination=traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#test get_traveler_location
test_destination_index=get_traveler_location(test_traveler)
#print(test_destination_index)

attractions=[[] for destination in destinations]
#test list comprehension above

def add_attraction(destination, attraction):
  try:
    destination_index=get_destination_index(destination)
  except ValueError:
    return
  attractions_for_destination=attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

#add attractions
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

#write a function find attractions that finds the most interesting places in new city for them

def find_attractions(destination, interests):
  destination_index=get_destination_index(destination)
  attractions_in_city=attractions[destination_index]
  attractions_with_interest=[]
  for attraction in range(0, len(attractions_in_city)):
    possible_attraction = attractions_in_city[attraction]
    attraction_tags=possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

#test find attractions
la_arts=find_attractions("Los Angeles, USA", ['art'])
la_art_and_beach=find_attractions("Los Angeles, USA", ['art', 'beach'])
#print(la_art_and_beach)

#make function that gets attractions for travelers based on the traveler.

def get_attractions_for_traveler(traveler):
  traveler_destination=traveler[1]
  traveler_interests=traveler[2]
  traveler_attractions=find_attractions(traveler_destination, traveler_interests)
  interests_string="Hi {name}, we think you'll like these places around {destination}: ".format(name=traveler[0], destination=traveler_destination, )
  for attraction in range(0,len(traveler_attractions)):
    interests_string+= (traveler_attractions[attraction]+", ")
    
  interests_string=interests_string[:-2]
  interests_string+="."
  return interests_string

#test get_attractions for traveler
#traveler2=['Dereck Smill', 'Paris, France', ['monument']]
traveler3=['Bob Barker', 'Paris, France', ['monument', 'art']]
#smills_france=get_attractions_for_traveler(traveler2)
#print(smills_france)
barker_france=get_attractions_for_traveler(traveler3)
print(barker_france)
    
  


