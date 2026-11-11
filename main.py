from pyscript import document   # type: ignore[reportMissingImports]

# Dictionary containing element information
# element symbol, element name, atomic number, atomic mass
nonmetals = {
    "H": ("H", "Hydrogen", 1, 1.008),
    "He": ("He", "Helium", 2, 4.003),
    "C": ("C", "Carbon", 6, 12.011),
    "N": ("N", "Nitrogen", 7, 14.007),
    "O": ("O", "Oxygen", 8, 15.999),
    "F": ("F", "Fluorine", 9, 18.998),
    "Ne": ("Ne", "Neon", 10, 20.180),
    "P": ("P", "Phosphorus", 15, 30.974),
    "S": ("S", "Sulfur", 16, 32.065),
    "Cl": ("Cl", "Chlorine", 17, 35.453),
    "Ar": ("Ar", "Argon", 18, 39.948),
    "Se": ("Se", "Selenium", 34, 78.971),
    "Br": ("Br", "Bromine", 35, 79.904),
    "Kr": ("Kr", "Krypton", 36, 83.798),
    "I": ("I", "Iodine", 53, 126.904),
    "Xe": ("Xe", "Xenon", 54, 131.293),
    "Rn": ("Rn", "Radon", 86, 222),
    "At": ("At", "Astatine", 85, 210),
}

# Function to search for an element
def find(e=None):
    # Get the input value from HTML
    nonmetal = document.getElementById("nonmetal").value.strip()
    symbol = nonmetal.upper() if nonmetal else ""

    # Get from the Dictionary, if the provided symbol is not listed, the system shall reply with "Unsupported Element Detected"
    result = nonmetals.get(symbol, ("Unsupported Element Detected", "Value Unknown", "Value Unknown", "Value Unknown"))

    # Display the result in HTML
    document.getElementById("symbol").innerText = result[0]
    document.getElementById("name").innerText = result[1]
    document.getElementById("number").innerText = result[2]
    document.getElementById("mass").innerText = result[3]

    # Reveal the result box once the button is pressed
    document.getElementById("result1").style.display = "block"