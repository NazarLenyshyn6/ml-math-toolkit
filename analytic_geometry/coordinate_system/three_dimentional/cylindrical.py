"""3d Cylindrical coordinate system point implementation."""

from __future__ import annotations

from typing_extensions import override

from pydantic import BaseModel
import numpy as np

from analytic_geometry.coordinate_system.base import CoordinatePoint
from analytic_geometry.coordinate_system.three_dimentional.cartesian import CartesianPoint_3d


class CylindricalPoint_3d(BaseModel, CoordinatePoint):
    """
    Represents a point in the 3d Cylindrical coordinate system.

    Attributes:
        name: A label or identifier for the point.
        r: ...
        theta: The ...
        h: ...
    """
    
    name: str
    r: float
    theta: float
    h: float
    
    @override
    def to_array(self) -> np.ndarray:
        """
        Convert the point to a NumPy array representation.

        Returns:
            np.ndarray: A 1D array of the form [r, θ, z].
        """
        return np.array([self.r, self.theta, self.h])
    
    def to_cartesian(self) -> CartesianPoint_3d:
        """
        Return the Cartesian representation of this point.

        Since the point is already in Cartesian form, it returns itself.

        Returns:
            CartesianPoint_3d: This instance.
        """
        x = self.r * np.cos(self.theta)
        y = self.r * np.sin(self.theta)
        z = self.h
        return CartesianPoint_3d(
            name=self.name,
            x=x,
            y=y,
            z=z
            )
        
    def euclidean_distanse_to(self, coordinate_point: CoordinatePoint) -> float:
        """
        Compute the Euclidean distance between this point and another coordinate point.

        Args:
            coordinate_point (CoordinatePoint): The other point.

        Returns:
            float: The Euclidean distance between the two points.

        Raises:
            TypeError: If the provided object is not a CoordinatePoint.
        """
        if not isinstance(coordinate_point, CoordinatePoint):
            raise TypeError("...")
        return self.to_cartesian().euclidean_distanse_to(coordinate_point)
    
    def visualize(self) -> None:
        """
        Visualize the point in 3d Cylindrical space.

        This is a stub. In a full implementation, it may use matplotlib or another library.
        """
        print("Todo...")
        
    def visualize_in_Cylindrical(self) -> None:
        """
        Visualize this point in the Cylindrical coordinate system.

        For 3d Cylindrical points, this is identical to `visualize()`.
        """
        self.to_cartesian().visualize()
