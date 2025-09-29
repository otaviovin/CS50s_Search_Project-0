# Degrees — Shortest Actor Connection

Find the shortest chain of movies that connects any two actors (the "Six Degrees" problem).  
This project loads a movie/actor dataset and uses **breadth-first search (BFS)** to compute the shortest path between two actors where each step is "Actor A and Actor B starred in Movie X".

> This repository is based on the CS50 AI `degrees` project distribution (small/large datasets).  
> Download distribution code (data): `https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip`

----------------------------------------------------------------------------------------------------

## Quick start

### Prerequisites
- Python 3.7+ (no external dependencies — uses only the Python standard library and CSV parsing)

### Run
From the project root (where `degrees.py` is located), choose a dataset folder (`small` or `large`) and run:

```bash
# run against the small dataset
python degrees.py small

# run against the large dataset
python degrees.py large
```

----------------------------------------------------------------------------------------------------

# Test with small:
```bash
python degrees.py small
```

## Test 1 - Example 
Name: Kevin Bacon
Name: Tom Hanks
1 degrees of separation.
1: Kevin Bacon and Tom Hanks starred in Apollo 13

## Test 2 - Example
Name: Jack Nicholson
Name: Sally Field
3 degrees of separation.
1: Jack Nicholson and Kevin Bacon starred in A Few Good Men
2: Kevin Bacon and Gary Sinise starred in Apollo 13
3: Gary Sinise and Sally Field starred in Forrest Gump

# Test with large: 
```bash
python degrees.py large
```

## Test 1 - Example
Name: Dan Aykroyd
Name: Clint Eastwood
2 degrees of separation.
1: Dan Aykroyd and James Garner starred in My Fellow Americans
2: James Garner and Clint Eastwood starred in Space Cowboys

## Test 2 - Example
Name: Salma Hayek
Name: Madonna
2 degrees of separation.
1: Salma Hayek and Antonio Banderas starred in Desperado
2: Antonio Banderas and Madonna starred in Evita

----------------------------------------------------------------------------------------------------


