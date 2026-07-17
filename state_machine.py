"""
state_machine.py

Industrial PLC State Machine
"""

from enum import Enum, auto


class MachineState(Enum):
    """
    PLC Operating States
    """

    IDLE = auto()
    RUNNING = auto()
    WAIT_FOR_BOX = auto()
    DETECT_BOX = auto()
    SORT_BOX = auto()
    REMOVE_BOX = auto()
    STOPPED = auto()
    EMERGENCY_STOP = auto()


class StateMachine:
    """
    Industrial PLC State Machine
    """

    def __init__(self):

        self.state = MachineState.IDLE

    # =====================================================

    def set_state(self, new_state):
        """
        Change state only when necessary.
        """

        if self.state == new_state:
            return

        print(f"[STATE] {self.state.name} -> {new_state.name}")

        self.state = new_state

    # =====================================================

    def get_state(self):

        return self.state

    # =====================================================

    def is_running(self):

        return self.state == MachineState.RUNNING

    # =====================================================

    def is_idle(self):

        return self.state == MachineState.IDLE

    # =====================================================

    def is_emergency(self):

        return self.state == MachineState.EMERGENCY_STOP

    # =====================================================

    def start(self):

        self.set_state(
            MachineState.RUNNING
        )

    # =====================================================

    def stop(self):

        self.set_state(
            MachineState.STOPPED
        )

    # =====================================================

    def wait_box(self):

        self.set_state(
            MachineState.WAIT_FOR_BOX
        )

    # =====================================================

    def detect_box(self):

        self.set_state(
            MachineState.DETECT_BOX
        )

    # =====================================================

    def sort_box(self):

        self.set_state(
            MachineState.SORT_BOX
        )

    # =====================================================

    def remove_box(self):

        self.set_state(
            MachineState.REMOVE_BOX
        )

    # =====================================================

    def emergency(self):

        self.set_state(
            MachineState.EMERGENCY_STOP
        )

    # =====================================================

    def reset(self):

        self.set_state(
            MachineState.IDLE
        )

    # =====================================================

    def status(self):

        print("\n========== STATE MACHINE ==========")

        print(
            "Current State :",
            self.state.name
        )

        print("===================================\n")