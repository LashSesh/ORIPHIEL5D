class Storage:
    def __init__(self):
        self.segments = {}

    def add_segment(self, segment_id, data):
        self.segments[segment_id] = data

    def get_all(self):
        return self.segments


storage = Storage()
