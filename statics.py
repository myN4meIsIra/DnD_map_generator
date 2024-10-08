#    materials:
materials = {
    "stone": [153, 170, 187],
    "stoneWall": [143, 160, 177],

    "wood": [99, 70, 45],
    'woodWall': [89, 60, 35],

    'forest' : [19, 76, 19],
    'forestWall' : [27, 107, 20],

    'wet': [97, 123, 159],
    'wetWall': [50, 83, 130],

    'plant': [53, 136, 86],
    'chest': [145, 119, 57],
}

# divided by the number of orientations of that item that can be generated, then multiply by 10 so we don't have 0-weights
weights = {
    "wall": round((3 / 3) * 10),
    "door": round((1 / 2) * 10),
    #'road': round((1 / 2) * 10),
    "tree": round((1 / 3) * 10),
    "floor": round((6 / 2) * 10),
}

chanceOfDecoration = 1/4
decorationWeights = {
    'plant':5,
    'chest':1,
}