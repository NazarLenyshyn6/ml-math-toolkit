# 1. What is a Coordinate System?
A coordinate system is a method for assigning numbers(called coordinates) to points in a space.These numbers describe where the point is, relative to a fixed reference.

At its core:
    A coordinate system translates geometric shapes into numerical representations, allowing us to apply algebra to geometry.

This is the heart of analytic geometry (or coordinate geometry) - a bridge between algebra and geometry.

# 2. Basic Types of Coordinate Systems
There are several types of coordinate systems, depending of the space and the symmetry of the problems we want to solve.

## 2.1 Cartesion Coordinate System (Rectangular Coordinates)
This is the most common and intuitive one.

* 2D Cartesian Plane:
    * Has two perpendiculat number lines: the x-axis(horizontal) and the y-axis (vertical)
    * The point of intersection is called the origin (0, 0)
    * Every point is described by an **ordered pair** (x, y) 

* 3D Cartesian Plane:
    * Adds a third axis, z, perpendicular to both x and y
    * Every point is described by an **ordered triplet*** (x, y, z)

* Key Properties:
    * Axes are perpendicular (orthogonal)
    * Units are uniform along each axis
    * Coordinates values can be both positive and negative

This is the system used in most analytic geometry.

## 2.2 Polar Coordinate System (in 2D):
Used when problems have circular symmetry:
* A point is defined by:
    * r: the distance from the origin()
    * θ: the angle from the positive x-axis (in radians or degrees)

So istead of (x, y) you descirbe very the same point as (r, θ)
* Conversions:
    * x = rcos(θ)
    * y = rsin(θ)

Useful in physics, signal processing, and circulaar motios problems

## 2.3 Cylindrical and Sprerical Coordinates (in 3D)
* a. Cylindrical Coordinates: Combines polar + z-axis
    * (r, θ, z)

* b Spherial Coordinates: For spherical symmetry
    * (ρ,θ,ϕ)
    * ρ: distance from origin
    * θ: azimute angle in the xy-plane
    * ϕ: polar angle from z-axis