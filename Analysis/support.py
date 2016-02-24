DEFAULT_KEY = None

color_matrix = {
    ("low", DEFAULT_KEY): 1,
    ("med", DEFAULT_KEY): 2,
    ("high", DEFAULT_KEY): 3,
    ("low", "low") : 1,
    ("med", "low") : 2,
    ("high", "low") : 3,
    ("low", "med") : 4,
    ("med", "med") : 5,
    ("high", "med") : 6,
    ("low", "high") : 7,
    ("med", "high") : 8,
    ("high", "high") : 9
}

index_matrix = {
    0 : "low",
    1: "med",
    2: "high",
}