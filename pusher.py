"""
pusher.py

Industrial Conveyor Pushers
"""


class Pusher:
    """
    Simulates left and right pneumatic pushers.
    """

    def __init__(self):

        self.left_active = False
        self.right_active = False

        self.left_count = 0
        self.right_count = 0

    # =====================================================
    # LEFT PUSHER
    # =====================================================

    def push_left(self, box):

        self.left_active = True

        print(
            f"[PUSHER] LEFT -> "
            f"Box ID={box.id} "
            f"Color={box.color} "
            f"Size={box.size}"
        )

        box.mark_sorted()

        self.left_count += 1

        self.left_active = False

    # =====================================================
    # RIGHT PUSHER
    # =====================================================

    def push_right(self, box):

        self.right_active = True

        print(
            f"[PUSHER] RIGHT -> "
            f"Box ID={box.id} "
            f"Color={box.color} "
            f"Size={box.size}"
        )

        box.mark_sorted()

        self.right_count += 1

        self.right_active = False

    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        self.left_active = False
        self.right_active = False

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        print("\n========== PUSHER STATUS ==========")
        print(f"Left Active  : {self.left_active}")
        print(f"Right Active : {self.right_active}")
        print(f"Left Count   : {self.left_count}")
        print(f"Right Count  : {self.right_count}")
        print("===================================\n")