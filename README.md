# OpenFOAM_testcases

## bullet2D
(OpenFOAM 6)

From [Ali Ikhsanul](https://www.youtube.com/watch?v=QDECc1yaRYI&list=PLSgiCo_OhhpNeJ9luyZEBflLpRm_IFW79) Salome & OpenFOAM tutorial

Mesh is generated with salome.

Base: compressible/sonicFoam/RAS/prism

Solver: sonicFoam

Turbulence model: RAS

## Flute simulation (case 1)
(OpenFOAM 6)

1. Geometry constructed with Rhino 6

2. Meshing tool snappyHexMesh

3. pimpleFoam solver

4. RAS turbulence model
#### Assumptions
1. Embouchure hole half inlet and half outlet.

2. Blow angle 45 degree to embouchure hole perpendicular.

## Flute simulation (case 2)
(OpenFOAM 6)
1. Geometry constructed with Rhino 6

2. Meshing tool snappyHexMesh

3. pimpleFoam

4. RAS turbulence model
#### Assumptions
1. Embouchure hole considered inlet only.

2. Blow angle 45 degree to embouchure hole perpendicular.

## Wigley Hull
(OpenFOAM 9)

1. Meshing tool snappyHexMesh

2. interFoam

3. RAS turbulence model

Source case: tutorials/multiphase/interFoam/DTCHull
