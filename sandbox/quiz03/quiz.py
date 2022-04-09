from __future__ import annotations


class ChristmasTreeFarm:

    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        self.plots = []
        i: int = 0
        while i < plots:
            self.plots.append(0)
            i += 1
        i = 0
        while i < initial_planting:
            self.plots[i] = 1
            i += 1
    
    def plant(self, index: int) -> None:
        self.plots[index] = 1
    
    def growth(self) -> None:
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                self.plots[i] += 1
            i += 1

    def harvest(self, replant: bool) -> int:
        count: int = 0
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] >= 5:
                count += 1
                if replant:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
            i += 1
        return count
        
    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        trees: int = 0
        for plot in self.plots:
            if plot > 0:
                trees += plot
        for plot in rhs.plots:
            if plot > 0:
                trees += plot
        return ChristmasTreeFarm(len(self.plots) + len(rhs.plots), trees)

