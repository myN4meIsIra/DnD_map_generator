# for positions, what types can create what
# wall, tree, door, road, floor
'''
    format:
    <cardinal direction of element>:{
        <if this was built there [h,v,c]<--orientation >:[
            # these things can be built
            {<element that can be built>:<orientation that can be built>}
        ]
    }

                            ceiling
                              |
                      left -- 0 -- right
                              |
                            floor
'''

rules = {
    "ceiling": {
        # walls
        "wall-c":[
            {'wall':'v'},
            {'door':'v'},
            {'wall':'c'},
        ],
        "wall-v":[
            {'wall':'v'},
            {'door':'v'},
            {'wall': 'c'},
        ],
        "wall-h":[
            {'floor':''},
            {'tree':''},
            {'wall': 'c'},
        ],

        # doors
        'door-h':[
            {'wall':'h'},
            {'floor':''},
            {'floor': ''},
            {'tree':''},
        ],
        'door-v':[
            {'wall':'v'},
            {"wall": 'c'},
            {'door':'v'}
        ],

        # roads
        'road-v':[
            {"wall":'v'},
            {'road':'v'},
            {'road':'c'},
            {'floor':''},
        ],
        'road-h':[
            {"wall":'h'},
            {'door':'h'},
            {'tree':''},
            {'floor':''},
        ],

        # un-oriented elements
        'floor-':[
            {'wall':'h'},
            {'door':'h'},
            {'wall': 'v'},
            {'door': 'v'},
            {'wall': 'c'},
            {'tree':''},
            {'floor': ''},
        ],
        'tree-':[
            {'tree':''},
            {'wall': 'h'},
            {'door': 'h'},
            {'wall': 'v'},
            {'door': 'v'},
            {'wall': 'c'},
            {'floor': ''},
        ],


    },

    # floor not used right now
    "floor": {    },

    'right': {
        # walls
        "wall-c":[
            {'wall':'h'},
            {'door':'h'},
            {'wall':'c'},
        ],
        "wall-v":[
            {'floor':''},
            {'tree':''},
            {'wall': 'c'},
        ],
        "wall-h":[
            {'wall':'v'},
            {'door':'v'},
            {'wall': 'c'},
        ],


        # doors
        'door-h':[
            {'wall':'v'},
            {"wall": 'c'},
            {'door':'v'}
        ],
        'door-v': [
            {'wall': 'h'},
            {'floor': ''},
            {'tree': ''},
        ],

        # roads
        'road-v':[
            {"wall":'h'},
            {'door':'h'},
            {'tree':''},
            {'floor':''},
        ],
        'road-h': [
            {"wall": 'v'},
            {'road': 'v'},
            {'road': 'c'},
            {'floor': ''},
        ],

        # un-oriented elements
        'floor-':[
            {'wall':'h'},
            {'door':'h'},
            {'wall': 'v'},
            {'door': 'v'},
            {'wall': 'c'},
            {'tree':''},
            {'floor': ''},
        ],
        'tree-':[
            {'tree':''},
            {'wall': 'h'},
            {'door': 'h'},
            {'wall': 'v'},
            {'door': 'v'},
            {'wall': 'c'},
            {'floor':''},
        ],
    },

    # left not used right now
    'left':{    },
}