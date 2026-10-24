import requests
import random

pokemons = [
    "pikachu",
    "bulbasaur",
    "charmander",
    "squirtle",
    "eevee",
]

api_url = "https://pokeapi.co/api/v2/pokemon/{}"
max_attempts = 3

def get_pokemon_data(pokemon_name):
    """Retrieve one Pokemon's data from PokeAPI."""
    url = api_url.format(pokemon_name)

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        pokemon = response.json()

        name = pokemon.get("name")
        height = pokemon.get("height")
        weight = pokemon.get("weight")

        if name is None or height is None or weight is None:
            print("The API response did not contain all required Pokemon data.")
            return None

        return {
            "name": name,
            "height": height,
            "weight": weight,
        }

    except requests.exceptions.HTTPError:
        print(f"Could not retrieve '{pokemon_name}'. The API returned "
              f"HTTP status {response.status_code}.")
    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")
    except ValueError:
        print("The API response was not valid JSON.")

    return None

def play_game():
    """Run one round of the Pokemon guessing game."""
    chosen_name = random.choice(pokemons)
    pokemon = get_pokemon_data(chosen_name)

    if pokemon is None:
        print("The game could not start. Please try again later.")
        return

    print("\nWho's THAT Pokemon?")
    print("Guess the Pokemon using its height and weight.")
    print(f"Height: {pokemon['height']} decimetres")
    print(f"Weight: {pokemon['weight']} hectograms")
    print(f"You have {max_attempts} attempts.")

    attempts = 0

    while attempts < max_attempts:
        guess = input(f"\nAttempt {attempts + 1}/{max_attempts} - Pokemon Name: ")
        guess = guess.strip().lower()

        if not guess:
            print("Please enter a Pokemon name.")
            continue

        if guess not in pokemons:
            print("That name isn't in this game's Pokemon list. Try one of the listed Pokemons.")
            print("Available choices: " + ", ".join(pokemons))
            continue

        attempts += 1

        if guess == pokemon["name"]:
            print("That's the Pokemon! <3 You win!")
            return

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"That's NOT the Pokemon! Attempts remaining: {remaining}")

    print(f"Sorry, out of attempts! The Pokemon was {pokemon['name'].title()}.")

if __name__ == "__main__":
    play_game()