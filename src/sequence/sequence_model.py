class SequenceModel:

    def __init__(self, sequence_id, steps):
        self.sequence_id = sequence_id
        self.steps = steps

    def expected(self):
        return self.steps
