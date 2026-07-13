# Step 02 - Electronics and Soldering

This step covers the soldering and initial electrical validation of the wiring, power connection, and the Raspberry Pi. The propellers must remain removed throughout this stage.

![Hexacopter wiring diagram](../hardware/wiring_diagrams/Hexa_Wiring_Diagram.svg)
Wiring diagram for the quadcopter can be found at: [Quad Wiring Diagram](../hardware/wiring_diagrams/Quad_Wiring_Diagram.svg)

## 1. Practise before using the final hardware

If you have limited soldering experience, practise first using spare flight controllers/ESCs, wires, or unused electronic components. This reduces the risk of damaging the flight controller, ESC, motors, or Raspberry Pi.

In this project, spare hardware was also used to become familiar with flight-controller firmware flashing and configurator software before working with the final components.

## 2. Review the wiring diagram

Before soldering, identify the following connections:

- six motors to the six ESC outputs;
- XT30 battery connector to the positive and negative ESC power pads;
- capacitor to the ESC power pads;
- flight controller to the ESC;
- Raspberry Pi communication wires:
  - 5 V;
  - ground;
  - flight-controller TX2;
  - flight-controller RX2.

Check the labels printed on the boards and compare them with the wiring diagram before applying heat. Do not rely only on wire colour.

> **Important:** TX and RX must be crossed between devices. The flight-controller TX wire connects to Raspberry Pi RX, and flight-controller RX connects to Raspberry Pi TX. Both devices must share a common ground.

## 3. Prepare a safe soldering workspace

Soldering was performed in a well-ventilated area. The following equipment was used:

- soldering iron;
- suitable solder;
- flux;
- wire cutters and strippers;
- tweezers or helping hands;
- heat-resistant work surface;
- multimeter;
- protective eyewear;
- solder extractor if available.

Avoid breathing solder fumes and do not touch recently soldered pads or components.

## 4. Solder the motors to the ESC

Each brushless motor has three phase wires. The three wires of each motor were soldered to one of the six ESC motor outputs.

At this stage, the order of the three phase wires is not critical because swapping any two phase wires reverses the motor direction. Motor direction can also be corrected later through ESC configuration, depending on the available software.

After soldering:

- inspect each joint for incomplete wetting;
- check that neighbouring pads are not bridged;
- gently pull each wire to confirm that it is mechanically secure;
- keep the wires long enough to reach the motors after final frame assembly.

## 5. Solder the battery connector and capacitor

The XT30 battery connector was soldered to the positive and negative power-input pads of the ESC. The polarity must match the 4S battery connector.

The capacitor was connected across the same power input:

- capacitor positive to ESC positive;
- capacitor negative to ESC ground.

Electrolytic capacitors are polarised. Reversing the capacitor may damage it or cause it to fail.

Before connecting a battery, use a multimeter to verify:

- correct battery-connector polarity;
- continuity where expected;
- no short circuit between the positive and negative power pads.

A smoke stopper or current-limited power supply is recommended for the first power-up when available.

## 6. Prepare the Raspberry Pi connection

Four wires were soldered to the selected flight-controller UART and power pads:

- 5 V;
- GND;
- RX2;
- TX2.

The opposite ends were connected to female header connectors so that the Raspberry Pi could later be connected and removed.

Male header pins were soldered to the Raspberry Pi Zero 2 W. Right-angled header pins are preferable when vertical clearance is limited because they reduce cable strain and simplify mounting. Straight headers were used in this project because suitable right-angled headers were unavailable.

The Raspberry Pi should not yet be connected unless its operating system has already been installed and its power requirements have been verified.

## 7. Connect the flight controller and ESC

The flight controller and ESC were connected using the stack connector supplied with the hardware. Before power-up, check that:

- the connector is aligned correctly;
- no pins are bent;
- the flight controller is not rotated relative to its intended orientation;
- no exposed wire can contact the board;
- the capacitor and battery leads are mechanically secure.

## 8. Perform the first electrical check

The first power-up was performed without propellers.

Before connecting the battery:

1. inspect all solder joints;
2. check for solder bridges;
3. verify XT30 polarity;
4. measure resistance between battery positive and ground;
5. ensure that loose wires cannot touch one another.

The 4S battery was then connected briefly. The ESC and flight controller LEDs were observed to confirm normal startup.

Disconnect the battery immediately if:

- a component becomes unusually hot;
- smoke or an unusual smell is detected;
- the boards do not start normally;
- the battery connector sparks excessively.

## Expected output

At the end of this step, you should have:

- six motors soldered to the ESC;
- the XT30 connector and capacitor installed;
- Raspberry Pi power and UART wires prepared;
- the flight controller connected to the ESC;
- no detected short circuits;
- successful initial power-up;

The electronics are now ready for final frame assembly and mounting.