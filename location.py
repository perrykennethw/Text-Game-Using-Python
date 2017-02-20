"""ADT for Location
"""
def make_locations(name, description, directions, location_names=[]):
    """Create and return a location."""
    return [name, description, directions, location_names]

def set_name(location, name):
    """Set the location's name."""
    location[0] = name
    return location

def set_description(location, description):
    """Set the location's description."""
    location[1] = description
    return location

def set_directions(location, directions):
    """Set the location's directions."""
    location[2] = directions
    return location

def get_name(location):
    """Return the name of the location."""
    return location[0][0]

def get_description(location, room_name):
    """Return the correct description for the room."""
    if room_name == "town gate":
        return location[0][1]
    if room_name == "town square":
        return location[1][1]
    if room_name == "book seller's":
        return location[2][1]
    if room_name == "shipyard":
        return location[3][1]
    if room_name == "court house":
        return location[4][1]
    if room_name == "outside":
        return location[5][1]

def get_directions(location, room_name):
    """Return the correct directions for the room."""
    if room_name == "town gate":
        return location[0][2]
    if room_name == "town square":
        return location[1][2]
    if room_name == "book seller's":
        return location[2][2]
    if room_name == "shipyard":
        return location[3][2]
    if room_name == "court house":
        return location[4][2]
    if room_name == "outside":
        return location[5][2]
    
def get_loc_name(location, directions):
    """Based on whatever direction is passed in, is what room will be returned."""
    if location[0][0] == "town gate":
        if directions == "N":
            location[0][0] = "town square"
            return location[0][0]
        elif directions == "S":
            location[0][0] = "outside"
            return location[0][0]
        elif directions == "E":
            location[0][0] = "book seller's"
            return location[0][0]
        elif directions == "W":
            location[0][0] = "shipyard"
            return location[0][0]
    if location[0][0] == "town square":
        if directions == "N":
            location[0][0] = "court house"
            return location[0][0]
        elif directions == "S":
            location[0][0] = "town gate"
            return location[0][0]
        elif directions == "E":
            location[0][0] = "shipyard"
            return location[0][0]
        elif directions == "W":
            location[0][0] = "town gate"
            return location[0][0]
    if location[0][0] == "book seller's":
        if directions == "N":
            location[0][0] = "book seller's"
            return location[0][0]
        elif directions == "S":
            location[0][0] = "book seller's"
            return location[0][0]
        elif directions == "E":
            location[0][0] = "book seller's"
            return location[0][0]
        elif directions == "W":
            location[0][0] = "town square"
            return location[0][0]
    if location[0][0] == "shipyard":
        if directions == "N":
            location[0][0] = "shipyard"
            return location[0][0]
        elif directions == "S":
            location[0][0] = "shipyard"
            return location[0][0]
        elif directions == "E":
            location[0][0] = "town square"
            return location[0][0]
        elif directions == "W":
            location[0][0] = "shipyard"
            return location[0][0]
    if location[0][0] == "court house":
        if directions == "N":
            location[0][0] = "court house"
            return location[0][0]
        if directions == "S":
            location[0][0] = "town square"
            return location[0][0]
        if directions == "E":
            location[0][0] = "court house"
            return location[0][0]
        if directions == "W":
            location[0][0] = "court house"
            return location[0][0]
    if location[0][0] == "outside":
        if directions == "N":
            location[0][0] = "town gate"
            return location[0][0]
        if directions == "S":
            location[0][0] = "outside"
            return location[0][0]
        if directions == "E":
            location[0][0] = "outside"
            return location[0][0]
        if directions == "W":
            location[0][0] = "outside"
            return location[0][0]
            
      
        
