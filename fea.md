---
title: Finite Element Analysis
author: Jasper Day
---

# Overview of Finite Element Analysis

1. Set up model
    - Generate mesh
    - Define material
    - Define boundary conditions
    - Define contact
    - Set up time integration
2. MESH CONVERGENCE
    - If you don't do this, people will come after you
    - Run the same simulation repeatedly with finer and finer meshes to ensure that the result converges
        - Run, refine, run, refine, repeat.
        - First mesh should "look about right" -- you should be able to see the grid on the surface of the mesh
    - Your elements should look like good cubes -- low aspect ratios
    - Use displacements or velocities, failing those use stress (more computationally difficult)

# Geometric Considerations

- Level of detail needed
    - You can often get rid of bolt holes, although make sure that you're keeping them within the stress concentration factors from literature

- 2D / symmetric / axisymmetric configuration
    - Some computational effort can be saved if you simplify (eg plane of loads, symmetric loading and material)

# Element Choice

Note different uses of elements:
- Shell, solid, beam (1d)
- Look out for *shear locking* in solid elements (triangle, quadrangle)
    - Underintegrate stress (fewer Gauss points) => hourglass modes (zero energy modes that grow with time and fuck up your mesh)
    - Solutions: SPI
- Good source for these -- check the ANSYS manual

