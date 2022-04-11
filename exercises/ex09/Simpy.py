"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union


__author__ = "730472629"


class Simpy:
    """GRade."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initiliazed Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """Produces a str representation of Simpy."""
        return f"Simpy({self.values})"
    
    def fill(self, x: float, count: int) -> None:
        """Mutates Simpy to having x value i times."""
        fill_list: list[float] = []
        for i in range(count):
            fill_list.append(x)
        self.values = fill_list
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in values attribute with range of values from start to stop with step intervals."""
        arange_list: list[float] = []
        i: float = start
        if step is None:
            step = 1.0
        assert step != 0
        while abs(i) < abs(stop):
            arange_list.append(i)
            i += step
        self.values = arange_list
    
    def sum(self) -> float:
        """Sums the values in Simpy object."""
        count: float = 0.0
        for num in self.values:
            count += num
        return count
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the addition operator."""
        add_list: list[float] = []
        i: int = 0
        while i < len(self.values):
            if isinstance(rhs, Simpy):
                add_list.append(self.values[i] + rhs.values[i])
            if isinstance(rhs, float):
                add_list.append(self.values[i] + rhs)
            i += 1
        return Simpy(add_list)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the power operator."""
        pow_list: list[float] = []
        i: int = 0
        while i < len(self.values):
            if isinstance(rhs, float):
                pow_list.append(self.values[i] ** rhs)
                i += 1
            if isinstance(rhs, Simpy):
                pow_list.append(self.values[i] ** rhs.values[i])
                i += 1
        return Simpy(pow_list)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads the equality operator."""
        result: list[bool] = []
        i: int = 0
        while i < len(self.values):
            if isinstance(rhs, Simpy):
                result.append(self.values[i] == rhs.values[i])
            if isinstance(rhs, float):
                result.append(self.values[i] == rhs)
            i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads the greater than operator and produces list of bools."""
        result: list[bool] = []
        i: int = 0 
        while i < len(self.values):
            if isinstance(rhs, Simpy):
                result.append(self.values[i] > rhs.values[i])
            if isinstance(rhs, float):
                result.append(self.values[i] > rhs)
            i += 1
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        if isinstance(rhs, list):
            result_list: list[float] = []
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    result_list.append(self.values[i])
                i += 1
            return Simpy(result_list)