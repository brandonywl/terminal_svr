from events import Events

class Move:
    def __init__(self, move_dict):
        self.turn = move_dict["turnInfo"]
        self.p2_units = move_dict["p2Units"]
        self.p2_stats = move_dict["p2Stats"]
        self.p1_units = move_dict["p1Units"]
        self.p1_stats = move_dict["p1Stats"]
        self.events = [Events(event_type, event_list) for event_type, event_list in move_dict["events"].items()]

    def __str__(self):
        return f"Turn {self.turn[-1]}, p1 Stats: {self.p1_stats}, p2 Stats: {self.p2_stats}"