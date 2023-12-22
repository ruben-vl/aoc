from __future__ import annotations
from abc import ABC, abstractmethod

class Module(ABC):
    
    @abstractmethod
    def handle_pulse(self, input: Module, high: bool) -> list[tuple[Module, bool]]:
        pass
    
class FlipFlopModule(Module):
    
    def __init__(self, name: str, destinations: set[Module]):
        self.name = name
        self.on = False
        self.destinations = destinations
    
    def handle_pulse(self, input: Module, high: bool) -> list[tuple[Module, bool]]:
        return_pulses = []
        if not high:
            self.on = not self.on
            for destination in self.destinations:
                return_pulses.append((self.name, destination, self.on))
        return return_pulses
            
class ConjunctionModule(Module):
    
    def __init__(self, name: str, inputs: set[Module], destinations: set[Module]):
        self.name = name
        self.memory = dict()
        for module in inputs:
            self.memory[module] = False
        self.destinations = destinations
    
    def handle_pulse(self, input: Module, high: bool) -> list[tuple[Module, bool]]:
        return_pulses = []
        self.memory[input] = high
        all_high = all(self.memory.values())
        for destination in self.destinations:
            return_pulses.append((self.name, destination, not all_high))
        return return_pulses

class BroadcastModule(Module):
    
    def __init__(self, name:str, destinations: set[Module]):
        self.name = name
        self.destinations = destinations

    def handle_pulse(self, input: Module, high: bool) -> list[tuple[Module, bool]]:
        return_pulses = []
        for destination in self.destinations:
            return_pulses.append((self.name, destination, high))
        return return_pulses

def part1(modules: dict[str, Module]):
    low_pulses = 0
    high_pulses = 0
    
    for i in range(1000):
        print(f"Push {i}")
        to_handle = [('broadcaster', None, False)]
        while len(to_handle) > 0:
            print(f"To Handle Amount: {len(to_handle)}")
            target, source, high = to_handle.pop(0)
            if high:
                high_pulses += 1
            else:
                low_pulses += 1
            returned_pulses = modules[target].handle_pulse(source, high)
            for pulse in returned_pulses:
                to_handle.append((pulse[0], target, pulse[1]))
            
    return low_pulses * high_pulses

if __name__ == "__main__":
    
    input_data = [l.strip().split(' -> ') for l in open("2023/python/day20_input.txt", 'r')]
    
    destinations: dict[str, list[str]] = dict()
    for name, dest_str in input_data:
        dests = dest_str.split(', ')
        destinations[name[1:]] = destinations
    
    modules: dict[str, Module] = dict()
    for name, dest_str in input_data:
        dests = dest_str.split(', ')
        match name[0]:
            case 'b':
                modules['broadcaster'] = BroadcastModule('broadcaster', dests)
            case '%':
                modules[name[1:]] = FlipFlopModule(name[1:], dests)
            case '&':
                inputs = [k for k, v in destinations.items() if name[1:] in v]
                modules[name[1:]] = ConjunctionModule(name[1:], inputs, dests)
    
    print(f"Part 1: {part1(modules)}")