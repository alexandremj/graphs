from dataclasses import dataclass

@dataclass
class Vertex:
    number: int
    label: str

    def __eq__(self, other):
        return (other and self.number == other.number
                and self.label == other.label)
    
    def __hash__(self):
        return hash(self.number)