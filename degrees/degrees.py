import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {} # nome -> {person_ids}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {} # person_id -> {name, birth, movies: set(movie_id)}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {} # movie_id -> {title, year, stars: set(person_id)}

def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass

def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")

    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")

    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

def shortest_path(source, target):
    """
    Finds the shortest path between two actors (source and target) in terms of co-starring in movies.

    Parameters:
        source (str): The IMDb ID of the source actor.
        target (str): The IMDb ID of the target actor.

    Returns:
        list of tuples: Each tuple is (movie_id, person_id) representing
                        a step in the path from source to target, where
                        the person starred in a movie with the next person.
                        The list is ordered from the source towards the target.
        None: If no path exists between source and target.

    Overview:
        This function implements a breadth-first search (BFS) algorithm to find the shortest
        connection path between two actors. BFS ensures the shortest path is found because it
        explores all neighbors at the current depth before moving to the next level.
    """

    # Step 1: Handle the trivial case where the source is the same as the target
    if source == target:
        return []

    # Step 2: Initialize the BFS frontier with the starting actor
    # The Node stores the current state (actor ID), the parent node, and the action (movie ID that connects parent to this actor)
    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier() # BFS uses a queue structure to explore in layers
    frontier.add(start)

    # Step 3: Keep track of explored actors to avoid revisiting
    explored = set()

    # Step 4: Perform BFS loop until the frontier is empty
    while not frontier.empty():
        # Remove the next node from the frontier for exploration
        node = frontier.remove()
        # Mark the current actor as explored
        explored.add(node.state)

        # Step 5: Explore all neighbors (actors who starred together in any movie)
        for movie_id, person_id in neighbors_for_person(node.state):
            # Skip if this actor has already been explored or is already in the frontier
            if person_id not in explored and not frontier.contains_state(person_id):
                # Create a new Node for this neighbor
                child = Node(state=person_id, parent=node, action=movie_id)

                # Step 6: If this neighbor is the target, reconstruct the path
                if person_id == target:
                    path = []
                    n = child
                    # Trace back from the target to the source
                    while n.parent is not None:
                        path.append((n.action, n.state))
                        n = n.parent
                    path.reverse()  # Reverse so it goes from source → target
                    return path

                # Step 7: Add the neighbor to the frontier for further exploration
                frontier.add(child)

    # Step 8: If the frontier is empty and no path was found, return raise
    return None

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]

def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors

if __name__ == "__main__":
    main()
