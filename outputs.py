"""
outputs.py

Industrial PLC Outputs
"""


class PLCOutputs:
    """
    Simulates PLC Digital Outputs
    """

    def __init__(self):

        # Machine Outputs
        self.motor = False

        # Pushers
        self.left_pusher = False
        self.right_pusher = False

        # Alarm
        self.alarm = False

        # Tower Lights
        self.green_light = False
        self.red_light = False

        # Statistics
        self.left_sorted = 0
        self.right_sorted = 0

    # =======================================================
    # Conveyor Motor
    # =======================================================

    def motor_on(self):

        if not self.motor:
            self.motor = True
            self.green_light = True
            print("[OUTPUT] Motor ON")

    def motor_off(self):

        if self.motor:
            self.motor = False
            self.green_light = False
            print("[OUTPUT] Motor OFF")

    # =======================================================
    # Pushers
    # =======================================================

    def push_left(self, box):

        self.left_pusher = True

        print(
            f"[LEFT PUSHER] "
            f"Box {box.id} "
            f"({box.color}, {box.size})"
        )

        self.left_sorted += 1

        self.left_pusher = False

    # -------------------------------------------------------

    def push_right(self, box):

        self.right_pusher = True

        print(
            f"[RIGHT PUSHER] "
            f"Box {box.id} "
            f"({box.color}, {box.size})"
        )

        self.right_sorted += 1

        self.right_pusher = False

    # =======================================================
    # Alarm
    # =======================================================

    def alarm_on(self):

        if not self.alarm:
            self.alarm = True
            self.red_light = True

            print("[OUTPUT] Alarm ON")

    def alarm_off(self):

        if self.alarm:
            self.alarm = False
            self.red_light = False

            print("[OUTPUT] Alarm OFF")

    # =======================================================
    # Reset Outputs
    # =======================================================

    def reset_outputs(self):

        self.motor = False

        self.left_pusher = False
        self.right_pusher = False

        self.alarm = False

        self.green_light = False
        self.red_light = False

    # =======================================================
    # Status
    # =======================================================

    def status(self):

        print("\n========== OUTPUT STATUS ==========")

        print("Motor        :", self.motor)
        print("Alarm        :", self.alarm)

        print("Green Light  :", self.green_light)
        print("Red Light    :", self.red_light)

        print("Left Sorted  :", self.left_sorted)
        print("Right Sorted :", self.right_sorted)

        print("===================================\n")