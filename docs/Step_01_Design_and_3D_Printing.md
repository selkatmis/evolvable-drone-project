# Step 01 - 3D Printing and Part Preparation

This step covers the preparation and printing of the structural drone parts. Full frame assembly is performed later, after the ESC, motors, power connector, and Raspberry Pi wiring have been soldered.

## 1. Generate or design the STL files

There are two options:

- Use the provided STL files in the [hardware/STL/](hardware/STL/) folder. (TBD)
- Design new parts in CAD and export them as STL files.

Designing new parts requires CAD experience, especially when working with meshes or adapting evolved morphologies.

## 2. Check design feasibility

Before printing, check whether the design is physically usable:

- neighbouring arms and propellers should not overlap;
- motor mounts should provide enough clearance for the propellers;
- the central plate should provide enough space for the FC/ESC stack;
- landing legs should provide enough ground clearance;
- tilted motors may require longer landing legs so the propellers remain above the ground.

For evolved or unconventional designs, these checks are especially important because small geometry changes can make the vehicle impossible or unsafe to assemble.

## 3. Choose the filament

Regular PLA can be used for prototypes, motor mounts, landing legs, and replacement parts. PETG-CF may be used for parts that require higher stiffness, such as arms or central plates.

Stiff arms are important because arm deformation changes the motor orientation and can affect the generated thrust direction.

PETG-CF should be handled carefully, especially around rough or damaged surfaces. Use gloves when handling unfinished parts, and follow the filament manufacturer's safety recommendations. 

In the tested platform, PETG-CF did not provide a clear practical advantage over standard PLA. Therefore, PLA may be preferred for parts because it is simpler to handle and produced comparable results under the conditions encountered in this project.

## 4. Print the parts

Slice the STL files using the settings appropriate for the selected filament and printer. In this project, the parts were printed using a Bambu Lab printer.

Also an good idea to check the manual before 3D printing: [3D printing manual](../hardware/3D_Printing_Manual.md)

Recommended checks after printing:

- no major warping;
- no cracks or weak layer adhesion;
- motor holes align with the motors;
- the right size screws fit in holes;
- arm holes align with the central plate;
- landing-leg holes align with the intended mounting points;
- parts are stiff enough for handling.

## 5. Prepare for later assembly

Do not complete the full frame assembly as soldering still needs to be performed. Keep the printed parts organised and label them if necessary.

At this stage, the expected output is a complete set of inspected printed parts ready for electronics assembly and final mounting.