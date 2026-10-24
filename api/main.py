import requests

request = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
 
pokemon = request.json()
 
name = pokemon.get('name')
height = pokemon.get('height')
weight = pokemon.get('weight')
 
print("Pokemon's Name: ???")
print(f"Pokemon's Height: {height}")
print(f"Pokemon's Weight: {weight}")
 
attempts = 0
run = True
while run == True:
    guess = input("Who's that Pokemon? ")
    if guess == name:
        print("That's the Pokemon! <3")
        break
    else:
        if attempts == 3:
            print(f"The Pokemon is {name}!")
        else:
            print("That's NOT the Pokemon!")
            attempts + 1