The native horizontal grid type, i.e., methods for distributing grid points over the sphere.

<details>
<summary>Click the arrow to learn more about the native horizontal grid type property options.</summary>

  - regular_latitude_longitude: a rectilinear latitude-longitude grid with evenly spaced latitude points and evenly spaced longitude points.
  - regular_gaussian: a Gaussian grid for which the number of longitudinal points is constant for each latitude.
  - reduced_gaussian: a Gaussian grid for which the number of longitudinal points is reduced as the poles are approached.
  - spectral_gaussian: a grid based on the transformation from spectral space to a reduced or nonreduced Gaussian grid.
  - spectral_reduced_gaussian: a grid based on the transformation from spectral space to a reduced Gaussian grid.
  - linear_spectral_gaussian: a spectral Gaussian grid for which the smallest spectral wavelength is represented by 2 grid points.
  - quadratic_spectral_gaussian: a spectral Gaussian grid for which the smallest spectral wavelength is represented by 3 grid points.
  - cubic_octahedral_spectral_reduced_gaussian: a spectral reduced Gaussian grid for which the smallest spectral wavelength is represented by 4 grid points, and which uses an octahedron-based method to reduce the number of grid points towards the poles.
  - rotated_pole: a regular latitude-longitude grid that is rotated to define a different north pole location.
  - stretched: a grid with higher resolution concentrated over an area of interest, at the expense of lower resolution elsewhere.
  - displaced_pole: an ocean grid whose poles are not antipodean, typically with the northern pole displaced to lie over land.
  - tripolar: a global curvilinear ocean grid with a southern pole and two northern poles all placed over land.
  - cubed_sphere: the spherical surface is defined as six coupled “logically square” regions.
  - icosahedral_geodesic: a grid that uses triangular tiles based on the subdivision of an icosahedron.
  - icosahedral_geodesic_dual: a grid that uses hexagonal and pentagonal tiles and is the dual of an icosahedral_geodesic grid.
  - yin_yang: two overlapping grid patches.
  - unstructured_triangular: an unstructured mesh consisting solely of triangles.
  - unstructured_polygonal: an unstructured mesh consisting of arbitrary polygons.
  - plane_projection: any transformation employed to represent the spherical surface of the globe on a plane.
  - none: there is no horizontal grid.

</details>
