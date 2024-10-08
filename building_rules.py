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

    elements of the format {-<element>:<orientation>} with '-' in the key position, are removed from possible build options in the selected orientation

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
            {'-floor':''},
            {'-wall':'h'},
            {'-door':'h'},
        ],
        "wall-v":[
            {'wall':'v'},
            {'door':'v'},
            {'wall': 'c'},
            {'-floor':''},
            {'-wall': 'h'},
            {'-door': 'h'},
        ],
        "wall-h":[
            {'floor':''},
            {'tree':''},
            {'wall': 'c'},
            {'-wall': 'v'},
            {'-door': 'v'},
        ],

        # doors
        'door-h':[
            {'wall':'h'},
            {'floor':''},
            {'floor': ''},
            {'tree':''},
            {'-wall': 'v'},
            {'-door': 'v'},
        ],
        'door-v':[
            {'wall':'v'},
            {"wall": 'c'},
            {'door':'v'},
            {'-wall': 'h'},
            {'-door': 'h'},
            {'-floor':''}
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
            {'wall': 'c'},
            {'tree':''},
            {'floor': ''},
            {'-wall': 'v'},
            {'-door': 'v'},
            #{'wall': 'c'},
        ],
        'tree-':[
            {'tree':''},
            {'wall': 'h'},
            {'door': 'h'},
            {'wall': 'c'},
            {'floor': ''},
            {'-wall': 'v'},
            {'-door': 'v'},
            #{'wall': 'c'},
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
            {'-floor': ''},
            {'-wall': 'v'},
            {'-door': 'v'},
        ],
        "wall-v":[
            {'floor':''},
            {'tree':''},
            {'wall': 'c'},
            {'-floor': ''},
            {'-wall': 'v'},
            {'-door': 'v'},
        ],
        "wall-h":[
            {'wall':'v'},
            {'door':'v'},
            {'wall': 'c'},
            {'-wall': 'v'},
            {'-door': 'v'},
        ],


        # doors
        'door-h':[
            {'wall':'v'},
            {"wall": 'c'},
            {'door':'v'},
            {'-wall': 'v'},
            {'-door': 'v'},
            {'-floor':''},
        ],
        'door-v': [
            {'wall': 'h'},
            {'floor': ''},
            {'tree': ''},
            {'-wall': 'h'},
            {'-door': 'h'},
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
            {'wall': 'v'},
            {'door': 'v'},
            {'tree':''},
            {'floor': ''},
            {'-wall': 'h'},
            {'-door': 'h'},
            #{'wall': 'c'},
        ],
        'tree-':[
            {'tree':''},
            {'wall': 'v'},
            {'door': 'v'},
            {'floor':''},
            {'-wall': 'h'},
            {'-door': 'h'},
            #{'wall': 'c'},
        ],
    },

    # left not used right now
    'left':{    },
}