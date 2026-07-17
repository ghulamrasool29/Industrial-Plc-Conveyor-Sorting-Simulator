"""
inputs.py

Industrial PLC Inputs
"""


class PLCInputs:
    """
    Simulates PLC Digital Inputs
    """

    def __init__(self):

        # Push Buttons
        self.start_pressed = False
        self.stop_pressed = False
        self.emergency_pressed = False

    # ======================================================
    # Push Buttons
    # ======================================================

    def press_start(self):

        self.start_pressed = True
        self.stop_pressed = False

        print("[INPUT] START Button Pressed")

    # ------------------------------------------------------

    def press_stop(self):

        self.stop_pressed = True
        self.start_pressed = False

        print("[INPUT] STOP Button Pressed")

    # ------------------------------------------------------

    def press_emergency(self):

        self.emergency_pressed = True

        print("[INPUT] EMERGENCY Button Pressed")

    # ------------------------------------------------------

    def reset_buttons(self):

        self.start_pressed = False
        self.stop_pressed = False

    # ======================================================
    # Sensors
    # ======================================================

    def box_present(self, box):

        return box is not None

    # ------------------------------------------------------

    def read_color(self, box):

        return box.color

    # ------------------------------------------------------

    def read_size(self, box):

        return box.size

    # ======================================================
    # Status
    # ======================================================

    def status(self):

        print("\n========== INPUT STATUS ==========")

        print("START     :", self.start_pressed)
        print("STOP      :", self.stop_pressed)
        print("EMERGENCY :", self.emergency_pressed)

        print("==================================\n")