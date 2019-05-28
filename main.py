# Exercise 3
from pathlib import Path
import utils as ut

# import functions from utils here

main_dir = Path("C:/Users/coral/Documents/GitHub/exercise-3-cwuestenhagen/")
data_dir = main_dir / "data"
output_dir = main_dir / "solution"

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

car_path = data_dir / "cars.txt"

# 2. Read the text file [2P]

with open(car_path, "r") as file:
    lines = file.read().splitlines()
print (lines)


# 3. Count the occurences of each item in the text file [2P]
        
ut.countValues(lines)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

ut.createDir(output_dir)

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]

ut.CountandCreate(lines, output_dir)