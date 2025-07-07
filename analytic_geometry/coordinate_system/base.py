"""Defines the abstract base class for points in any coordinate system."""

from __future__ import annotations


from abc import ABC, abstractmethod
from typing import Any, Tuple

import numpy as np

class CoordinatePoint(ABC):
    """
    Abstract base class for a point in a coordinate system.

    All subclasses must implement conversion to Cartesian coordinates,
    visualization, and tuple representation.
    """
    
    @abstractmethod
    def __init__(self, name: str, *coordinates: float):
        """
        Initialize the point with a name and coordinate values.
        
        Args:
            name (str): The name or label of the point.
            coordinates (float): One or more coordinate values.
        """
        ...
        
    def __eq__(self, other: Any) -> bool:
        """
        Compare two coordinate points for equality based on Cartesian coordinates.

        Args:
            other (Any): Another object to compare.

        Returns:
            bool: True if equivalent in Cartesian space, False otherwise.
        """
        if not isinstance(other, CoordinatePoint):
            return False
        return np.array_equal(self.to_cartesian().to_array(), other.to_cartesian().to_array())
        
    @abstractmethod
    def to_array(self) -> np.ndarray:
        """
        Convert the point to a tuple of coordinate values.

        Returns:
            np.ndarray: Array with coordinates values.
        """
        ...
        
    @abstractmethod
    def to_cartesian(self) -> CoordinatePoint:
        """
        Convert the point to its equivalent in Cartesian coordinates.

        Returns:
            CoordinatePoint: The Cartesian representation of this point.
        """
        
    @abstractmethod
    def euclidean_distanse_to(self, coordinate_point: CoordinatePoint) -> float:
        ...
        
    @abstractmethod
    def visualize(self) -> None:
        """
        Visualize the point in its native coordinate system.

        May raise a NotImplementedError for high-dimensional points.
        """
        ...
        
    def visualize_in_cartesian(self) -> None:
        """
        Visualize the point in the Cartesian coordinate system.

        May raise a NotImplementedError for high-dimensional points.
        """
        self.to_cartesian().visualize()
        
