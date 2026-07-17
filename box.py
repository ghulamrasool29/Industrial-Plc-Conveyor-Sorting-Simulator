"""
box.py

Industrial Conveyor Box
"""

from itertools import count


class Box:
    """
    Represents one box travelling on the conveyor.
    """

    _id_generator = count(1)

    def __init__(self, color, size):

        self.id = next(Box._id_generator)

        self.color = color.upper()

        self.size = size.upper()

        self.detected = False

        self.sorted = False

    # =====================================

    def mark_detected(self):

        self.detected = True

    # =====================================

    def mark_sorted(self):

        self.sorted = True

    # =====================================

    def reset(self):

        self.detected = False
        self.sorted = False

    # =====================================

    def info(self):

        return {
            "id": self.id,
            "color": self.color,
            "size": self.size,
            "detected": self.detected,
            "sorted": self.sorted
        }

    # =====================================

    def __str__(self):

        return (
            f"Box("
            f"ID={self.id}, "
            f"Color={self.color}, "
            f"Size={self.size})"
        )