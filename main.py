class ExitNotFoundError(Exception):
    def __init__(self, room_name):
        self.room_name = room_name
        super().__init__(f"{room_name} -> Room not found")

class Room: #Utilizing Room class to determine the def functions to find rooms
    def __init__(self, name, description, exits=[]):
        self.name = name
        self.description = description
        self.exits = exits

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_exits(self):
        return self.exits

    def list_exits(self):
        return "\n".join(self.exits)

    def __str__(self):
        return f"{self.name}: {self.description}\nExits:\n{self.list_exits()}\n"

class AdventureMap: #Creates a class for AdventureMap which helps us layout the map of all the rooms, and what is not a part of the map does not get found.
    def __init__(self):
        self.map = {}

    def add_room(self, room):
        self.map[room.name.lower()] = room

    def get_room(self, room_name):
        room_name_lower = room_name.lower()
        if room_name_lower in self.map:
            return self.map[room_name_lower]
        else:
            raise ExitNotFoundError(room_name)

    def __str__(self):
        room_list = "\n".join([str(room) for room in self.map.values()])
        return f"Adventure Map:\n{room_list}"

def main(): #Main function to be executed through the adventuremap
    print("Welcome to the Adkins house! Entering the study room. To leave the house, please type exit to jump out of the nearest window.\n")

    adventure_map = AdventureMap()
    room_data = [ #List for the rooms
        ("Guest Room", "A room filled with numerous torture devices. Who said anything about welcome guests?", ['Kitchen']),
        ("Library", "Better version of the study. It has all of the different books that one may want. Make sure that you stay quiet or the mean librarian will slap you!", ["Holodeck", "Trophy Room", "Study"]),
        ("Kitchen", "This amazing culinary art studio has it all: cheese cellar, wine racks, and a 16 stove burner. With its pizza oven, it makes for the perfect Italian getaway.", ["Study", "Guest Room"]),
        ("Study", "Do you love being disturbed while working? This room has it all. It is the central hub to the whole house. It has a giant wall of computers and amazing lighting, but doors that exit out into numerous different rooms.", ["Kitchen", "Library", "Bedroom"]),
        ("Holodeck", "A room that can disguise itself in a variety of ways. Experience a lush, humid rainforest, a speakeasy of the 1920’s, or the dungeons of Cooper Library.", ["Library"]),
        ("Trophy Room", "Spacious room with oak wood as far as the eye can see, shelves filled to the brim with trophies and obscure collections, it really makes you wonder who they belong to.", ["Bedroom", "Library"]),
        ("Bedroom", "A lavished bed adorns the center of this room, with long curtains, beautiful rugs, and gilded furniture acting as little details to truly make this a great bedroom.", ["Study", "Trophy Room"])
    ]

    for room_name, room_description, room_exits in room_data: #Preparing to get all the information for the rooms
        room = Room(room_name, room_description, room_exits)
        adventure_map.add_room(room)

    current_room = adventure_map.get_room("Study")  # Starting in the Study room

    while True:
        print(f"{current_room.name}: {current_room.description.strip()}") # Room's description and exits
        print("Exits:")
        print("\n".join(current_room.get_exits()).strip())
        while True:
            user_input = input("Please choose an exit: \n").lower().strip()  # input becomes lowercase
            if user_input == "exit": #Exits the user
                print("Exiting the house out of the nearest window... thanks for the tour!")
                break
  
            if user_input in [exit.lower() for exit in current_room.get_exits()]: #Input validation
                next_room_name = [exit for exit in current_room.get_exits() if exit.lower() == user_input][0] #Finds the room and updates the current room
                current_room = adventure_map.get_room(next_room_name)
                break
            else:
                print(f"{user_input} -> Room not found")  #If room could not be found in room_data

if __name__ == "__main__":
    main()