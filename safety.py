"""
safety.py

Industrial PLC Safety System
"""


class SafetySystem:
    """
    Handles all safety related operations.
    """

    def __init__(self, inputs, outputs):

        self.inputs = inputs
        self.outputs = outputs

        self.emergency_active = False

    # =====================================================

    def check_emergency_stop(self):
        """
        Check Emergency Stop status.
        Returns True if machine can run.
        """

        if self.inputs.emergency_pressed:

            if not self.emergency_active:

                self.emergency_active = True

                self.outputs.motor_off()

                self.outputs.alarm_on()

                print("\n******** EMERGENCY STOP ********")
                print("Machine Locked")
                print("*******************************\n")

            return False

        return True

    # =====================================================

    def reset_emergency(self):
        """
        Reset Emergency Stop
        """

        self.inputs.emergency_pressed = False

        self.emergency_active = False

        self.outputs.alarm_off()

        print("\nEmergency Reset Successful\n")

    # =====================================================

    def machine_ready(self):
        """
        Check if machine is ready.
        """

        return not self.emergency_active

    # =====================================================

    def emergency_status(self):
        """
        Return emergency status.
        """

        return self.emergency_active

    # =====================================================

    def status(self):

        print("\n========== SAFETY ==========")

        print(
            "Emergency :",
            self.emergency_active
        )

        print(
            "Machine Ready :",
            self.machine_ready()
        )

        print("============================\n")