from setuptools import setup, find_packages

# Read the contents of your README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="vodex",
    version="0.0.0",
    author="Aryan-code-commits",
    author_email="arayan.anantkumar.gupta@gmail.com",
    description="FastAPI CRUD Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aryan-code-commits/VodexAI-Assignment",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        'console_scripts': [
            'run-vodex=vodex.run_vodex:main',  # Change to your main app entry point
        ],
    },
    # install_requires=requirements,  # Use the requirements from the file
)
