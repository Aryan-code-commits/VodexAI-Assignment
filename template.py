import os
from pathlib import Path

# List of files to be created directly in the 'src/vodex' directory and 'routers' folder
list_of_files = [
    "src/vodex/main.py",
    "src/vodex/models.py",
    "src/vodex/database.py",
    "src/vodex/requirements.txt",
    "src/vodex/setup.py",
    "src/vodex/routers/items.py",    # Place items.py in 'routers'
    "src/vodex/routers/clock_in.py"  # Place clock_in.py in 'routers'
]

# Ensure the 'src/vodex' and 'src/vodex/routers' directories exist before creating the files
app_dir = Path("src/vodex")
routers_dir = Path("src/vodex/routers")

for directory in [app_dir, routers_dir]:
    if not directory.exists():
        os.makedirs(directory)
        print(f"Directory '{directory}/' created.")

# Create files in the 'src/vodex' directory and 'routers' folder
for filepath in list_of_files:
    filepath = Path(filepath)

    # Create the files if they don't exist or are empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            # You can add file-specific content here if needed
            pass
        print(f"Creating empty file: {filepath}")
    else:
        print(f"File already exists: {filepath}")
