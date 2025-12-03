# VibePad Gaming 🎮

A Discord and gaming-focused macropad built for the [Hack Club Hackpad](https://hackclub.com) event.

![VibePad Gaming Overview](/Assets/CADModelPreview.png)

## About This Project

This is my **first ever PCB design and 3D modeling project**! I followed the Hackpad tutorial closely since I had no prior experience with PCB design or CAD modeling. While the design is similar to the tutorial, this project served as my introduction to hardware design, and I'm grateful to Hack Club for giving me this opportunity to learn.

I'm excited to continue studying PCB design and 3D modeling in depth, and this macropad is just the beginning of my hardware journey!

## Features

- **4-button layout** optimized for Discord and gaming controls
- **5 customizable layers**: Base, Discord, Game, Media, and LED
- **Smart RGB lighting** with layer-based colors
- **Discord shortcuts** for mute, deafen, and streaming
- **Gaming layer** with toggle modifiers (Shift/Ctrl) and auto-clicker
- **Media controls** for music playback
- **LED modes**: Layer-based colors, breathing rainbow, or off

## Hardware

### PCB Design
![PCB Layout](/Assets/PCBPreview.png)

### Schematic
![Schematic](/Assets/SchematicPreview.png)

### 3D Enclosure
![3D Model](/Assets/CADModelPreview.png)

## Bill of Materials (BOM)

| Component | Quantity | Notes |
|-----------|----------|-------|
| Seeed XIAO RP2040 | 1 | Microcontroller (mounted through-hole) |
| MX-Style Switches | 4 | Mechanical keyboard switches |
| SK6812 MINI-E LEDs | 2 | RGB underglow/lighting |
| Blank DSA Keycaps (White) | 4 | Key covers |
| M3x16mm Screws | 4 | Case mounting |
| M3x5mx4mm Heatset Inserts | 4 | Threaded case inserts |
| 3D Printed Case | 1 | Custom enclosure |

## Firmware

The VibePad runs on [KMK Firmware](http://kmkfw.io/), a CircuitPython-based keyboard firmware.

### Layer Configuration

**Base Layer (Green):**
- Button 1: Switch to Discord layer
- Button 2: Switch to Game layer
- Button 3: Switch to Media layer
- Button 4: Switch to LED layer

**Discord Layer (Blue):**
- Button 1: Mute/Unmute (Ctrl+Shift+M)
- Button 2: Deafen/Undeafen (Ctrl+Shift+D)
- Button 3: Start/Stop Stream (Ctrl+Shift+S)
- Button 4: Return to Base layer

**Game Layer (Red):**
- Button 1: Toggle Shift (hold/release)
- Button 2: Toggle Ctrl (hold/release)
- Button 3: Auto-clicker (hold to spam left click)
- Button 4: Return to Base layer

**Media Layer (Yellow):**
- Button 1: Play/Pause
- Button 2: Next Track
- Button 3: Previous Track
- Button 4: Return to Base layer

**LED Layer (Cyan):**
- Button 1: Layer color mode
- Button 2: Breathing rainbow mode
- Button 3: LEDs off
- Button 4: Return to Base layer

### Installation

1. Flash CircuitPython on your XIAO RP2040
2. Install KMK firmware
3. Copy the `code.py` file to your board
4. Customize keymaps as needed!

## Assembly Notes

1. Solder the XIAO RP2040
2. Solder SK6812 LEDs
3. Insert heatset inserts into the 3D printed case
4. Mount switches into the case
5. Attach PCB and secure with M3 screws
6. Add keycaps and enjoy!

## Acknowledgments

Huge thanks to [Hack Club](https://hackclub.com) for the Hackpad program! This project taught me the fundamentals of PCB design, 3D modeling, and firmware development. I'm excited to continue learning and building more hardware projects!
---

**First PCB? First 3D model? No problem!** This project proves anyone can start learning hardware design. If you're interested in building your own, check out the [Hackpad program](https://hackclub.com)!