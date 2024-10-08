#    materials:
materials = {
    "stone": [153, 170, 187],
    "stoneWall": [143, 160, 177],

    "wood": [99, 70, 45],
    'woodWall': [89, 60, 35],

    'plant': [53, 136, 86],
}

# divided by the number of orientations of that item that can be generated, then multiply by 10 so we don't have 0-weights
weights = {
    "wall": round((1 / 3) * 10),
    "door": round((1 / 2) * 10),
    'road': round((1 / 2) * 10),
    "tree": round((1 / 2) * 10),
    "floor": round((4 / 2) * 10),
}