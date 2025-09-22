# Test with small
```bash
python degrees.py small
```

## Test 1
Name: Kevin Bacon
Name: Tom Hanks
1 degrees of separation.
1: Kevin Bacon and Tom Hanks starred in Apollo 13

## Test 2
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

## Test 1
Name: Dan Aykroyd
Name: Clint Eastwood
2 degrees of separation.
1: Dan Aykroyd and James Garner starred in My Fellow Americans
2: James Garner and Clint Eastwood starred in Space Cowboys

## Test 2
Name: Salma Hayek
Name: Madonna
2 degrees of separation.
1: Salma Hayek and Antonio Banderas starred in Desperado
2: Antonio Banderas and Madonna starred in Evita

----------------------------------------------------------------------------------------------------

# Submission Instructions (Commented for Reference)

## Git Configuration
# Set your global Git username
```bash
git config --global user.name "Otavio Bacovis"
```
# Set your global Git email
```bash
git config --global user.email "otavio_bacovis@hotmail.com"
```

## Navigate to your project directory
```bash
cd "C:\Python_Projects\Projetos\Harvard CS50's Introduction to Artificial Intelligence with Python - Search - Project 0\degrees"
```

## Initialize Git repository (if not already initialized)
```bash
git init
```

## Add remote repository
# If remote does not exist:
```bash
git remote add origin https://github.com/me50/otaviovin.git
```
# If remote exists and you want to update it:
```bash
git remote set-url origin https://github.com/me50/otaviovin.git
```

## Stage files for commit
```bash
git add degrees.py util.py small/ large/
```

## Commit your changes
```bash
git commit -m "Submit Project 0: Degrees"
```

## Set the main branch (if needed)
```bash
git branch -M main
```

## Push changes to GitHub
```bash
git push -u origin main --force
```
```bash
git push origin main:ai50/projects/2024/x/degrees
```

# After pushing, your project will be available on GitHub at: https://github.com/me50/otaviovin.git


