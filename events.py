class Events:
    def __init__(self, event_type, event_list):
        self.event_type = event_type
        self.event_list = event_list

    def __str__(self):
        if len(event_list) == 0:
            return f"No {self.event_type}"

        return f"{self.event_type}: {self.event_list}"