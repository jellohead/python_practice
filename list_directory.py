import os
import glob

directory_path = "/Users/patescalona/Projects/Games/Analogue Pocket/Roms/gameboy-color-romset-ultra-us"
search_term = "/*[lL]ink*"

search_path_and_term = directory_path + search_term
print(f"What I'm searching for:\n{search_path_and_term}")

# list contents of directory
list_of_files = os.listdir(directory_path)

print(f"List of files in directory:\n{list_of_files}\n")


# list files with specific name

specific_list_of_files = glob.glob(
    "/Users/patescalona/Projects/Games/Analogue Pocket/Roms/gameboy-color-romset-ultra-us/*[lL]ink*"
)

print(f"Specific list of files:\n{specific_list_of_files}")

specific_list_of_files = glob.glob(search_path_and_term)
print(f"Specific list of files:\n{specific_list_of_files}")

for specific_file in glob.glob(
    "/Users/patescalona/Projects/Games/Analogue Pocket/Roms/gameboy-color-romset-ultra-us/*[lL]ink*"
):
    print(specific_file)
