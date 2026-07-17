"""
conveyor.py

Industrial Conveyor Simulation
"""

from collections import deque


class Conveyor:
    """
    Industrial Conveyor Belt Simulation
    """

    def __init__(self):

        # Conveyor State
        self.running = False

        # Queue of boxes
        self.box_queue = deque()

        # Statistics
        self.total_processed = 0

    # ------------------------------------------------

    def start(self):
        """
        Start Conveyor
        """

        if not self.running:
            self.running = True
            print("[CONVEYOR] STARTED")

    # ------------------------------------------------

    def stop(self):
        """
        Stop Conveyor
        """

        if self.running:
            self.running = False
            print("[CONVEYOR] STOPPED")

    # ------------------------------------------------

    def is_running(self):
        """
        Return conveyor status
        """

        return self.running

    # ------------------------------------------------

    def add_box(self, box):
        """
        Add new box to conveyor
        """

        self.box_queue.append(box)

        print(
            f"[CONVEYOR] Box Added | "
            f"ID={box.id} "
            f"Color={box.color} "
            f"Size={box.size}"
        )

    # ------------------------------------------------

    def has_box(self):
        """
        Check if conveyor contains any box
        """

        return len(self.box_queue) > 0

    # ------------------------------------------------

    def get_current_box(self):
        """
        Peek first box
        """

        if self.has_box():
            return self.box_queue[0]

        return None

    # ------------------------------------------------

    def remove_box(self):
        """
        Remove processed box
        """

        if not self.has_box():
            return None

        box = self.box_queue.popleft()

        self.total_processed += 1

        print(
            f"[CONVEYOR] Removed Box ID={box.id}"
        )

        return box

    # ------------------------------------------------

    def clear(self):
        """
        Remove all boxes
        """

        self.box_queue.clear()

    # ------------------------------------------------

    def count(self):
        """
        Total boxes currently on conveyor
        """

        return len(self.box_queue)

    # ------------------------------------------------

    def status(self):
        """
        Print Conveyor Status
        """

        print("\n========== CONVEYOR ==========")
        print("Running :", self.running)
        print("Boxes   :", self.count())
        print("Processed :", self.total_processed)
        print("==============================\n")