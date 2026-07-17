"""
sensor.py

Industrial Sensor Simulation
"""


class Sensor:
    """
    Simulates industrial sensors used on the conveyor.
    """

    def __init__(self):

        self.presence_sensor = True
        self.color_sensor = True
        self.size_sensor = True

    # =====================================================
    # Presence Sensor
    # =====================================================

    def detect_box(self, box):

        if not self.presence_sensor:
            return False

        return box is not None

    # =====================================================
    # Color Sensor
    # =====================================================

    def read_color(self, box):

        if not self.color_sensor or box is None:
            return None

        return box.color

    # =====================================================
    # Size Sensor
    # =====================================================

    def read_size(self, box):

        if not self.size_sensor or box is None:
            return None

        return box.size

    # =====================================================
    # Sensor Failure Simulation
    # =====================================================

    def fail_presence_sensor(self):
        self.presence_sensor = False

    def repair_presence_sensor(self):
        self.presence_sensor = True

    def fail_color_sensor(self):
        self.color_sensor = False

    def repair_color_sensor(self):
        self.color_sensor = True

    def fail_size_sensor(self):
        self.size_sensor = False

    def repair_size_sensor(self):
        self.size_sensor = True

    # =====================================================
    # Status
    # =====================================================

    def status(self):

        print("\n========== SENSOR STATUS ==========")
        print(f"Presence Sensor : {'OK' if self.presence_sensor else 'FAILED'}")
        print(f"Color Sensor    : {'OK' if self.color_sensor else 'FAILED'}")
        print(f"Size Sensor     : {'OK' if self.size_sensor else 'FAILED'}")
        print("===================================\n")