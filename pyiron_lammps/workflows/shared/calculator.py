from abc import ABC


class Calculator(ABC):
    def generate_structures(self):
        raise NotImplementedError

    def analyse_structures(self, output_dict):
        raise NotImplementedError
