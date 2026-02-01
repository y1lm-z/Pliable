#!/usr/bin/env python
"""
Pliable - Direct BREP modeler
Stage 1: Display a cube
"""

from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

def main():
    # Initialize display
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Create a 100x100x100mm cube
    cube = BRepPrimAPI_MakeBox(100, 100, 100).Shape()

    # Display it
    display.DisplayShape(cube, update=True)
    display.FitAll()

    print("Cube displayed. Use mouse to:")
    print("  - Left drag: Rotate")
    print("  - Right drag: Pan")
    print("  - Scroll: Zoom")

    # Start the event loop
    start_display()

if __name__ == "__main__":
    main()
