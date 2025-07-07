"""3d Cartesian coordinate system point implementation."""

from __future__ import annotations

from typing_extensions import override

from pydantic import BaseModel
import numpy as np

from analytic_geometry.coordinate_system.base import CoordinatePoint


class CartesianPoint_3d(BaseModel, CoordinatePoint):
    """
    Represents a point in the 3d Cartesian coordinate system.

    Attributes:
        name: A label or identifier for the point.
        x: The X-coordinate.
        y: The Y-coordinate.
    """
    
    name: str
    x: float
    y: float
    z: float
    
    @override
    def to_array(self) -> np.ndarray:
        """
        Convert the point to a NumPy array representation.

        Returns:
            np.ndarray: A 1D array of the form [x, y].
        """
        return np.array([self.x, self.y, self.z])
    
    def to_cartesian(self) -> CartesianPoint_3d:
        """
        Return the Cartesian representation of this point.

        Since the point is already in Cartesian form, it returns itself.

        Returns:
            CartesianPoint_3d: This instance.
        """
        return self
        
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
        coordinate_point_in_cartisian = coordinate_point.to_cartesian()
        return np.sqrt(np.sum((self.to_array() - coordinate_point_in_cartisian.to_array()) ** 2))
    
    def visualize(self) -> None:
        """
        Visualize the point in 3d Cartesian space.

        This is a stub. In a full implementation, it may use matplotlib or another library.
        """
        print("Todo...")
        
    def visualize_in_cartesian(self) -> None:
        """
        Visualize this point in the Cartesian coordinate system.

        For 3d Cartesian points, this is identical to `visualize()`.
        """
        self.visualize()
