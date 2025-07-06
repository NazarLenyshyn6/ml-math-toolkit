"""."""

from __future__ import annotations

from typing_extensions import override

from pydantic import BaseModel, Field
import numpy as np

from analytic_geometry.coordinate_system.base import CoordinatePoint
from analytic_geometry.coordinate_system.two_dimentional.cartesian import CartesianPoint_2d

class PolarPoint_2d(BaseModel, CoordinatePoint):
    """Represents a point in 2D polar coordinate system.

    Attributes:
        name: Name or identifier of the point.
        r: Radial distance from the origin (must be ≥ 0).
        theta: Angle in radians between 0 and 2π inclusive.
    """
    
    name: str
    r: float = Field(ge=0)
    theta: float = Field(ge=0, le=np.pi * 2)
    
    def __setattr__(self, key, value):
        """Set attribute values with validation for 'r' and 'theta'.

        Args:
            key: Attribute name to set.
            value: Value to assign to the attribute.

        Raises:
            ValueError: If 'r' is negative or 'theta' is out of valid range.
        """
        if key == "r":
            if value < 0:
                raise ValueError("Radius 'r' must be non-negative.")
        elif key == "theta":
            if not (value >= 0 and value <= 2 * np.pi):
                raise ValueError("Angle 'theta' must be in [0, 2π].")
        super().__setattr__(key, value)
    
    @override
    def to_array(self) -> np.ndarray:
        """Return the polar coordinates as a numpy array [r, theta].

        Returns:
            np.ndarray: Array containing [r, theta].
        """
        return np.array([self.r, self.theta])
    
    @override
    def to_cartesian(self) -> CartesianPoint_2d:
        """Convert this polar point to its equivalent CartesianPoint_2d.

        Returns:
            CartesianPoint_2d: Cartesian coordinates corresponding to this polar point.
        """
        x = self.r * np.cos(self.theta)
        y = self.r * np.sin(self.theta)
        return CartesianPoint_2d(
            name=self.name,
            x=x,
            y=y
            )
        
    @override
    def euclidean_distanse_to(self, coordinate_point: CoordinatePoint) -> float:
        """Calculate Euclidean distance from this point to another coordinate point.

        Args:
            coordinate_point (CoordinatePoint): Another coordinate point to calculate distance to.

        Returns:
            float: Euclidean distance between the two points.
        """
        return self.to_cartesian().euclidean_distanse_to(coordinate_point)
        
    @override
    def visualize(self) -> None:
        """Visualize this point in the polar coordinate system.

        Note:
            Implementation is pending.
        """
        print("Todo...")
        
    @override
    def visualize_in_cartesian(self) -> None:
        """Visualize this point in Cartesian coordinate system."""
        self.to_cartesian().visualize()
        
    
    
