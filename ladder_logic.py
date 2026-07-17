"""
ladder_logic.py

Industrial PLC Ladder Logic
PART 1 / 2
"""

import time
from plc.state_machine import MachineState


class LadderLogic:

    def __init__(
        self,
        conveyor,
        inputs,
        outputs,
        safety,
        state_machine
    ):

        self.conveyor = conveyor
        self.inputs = inputs
        self.outputs = outputs
        self.safety = safety
        self.state_machine = state_machine

        self.dashboard = None

    # =====================================================

    def execute_cycle(self):

        # -----------------------------
        # Emergency
        # -----------------------------

        if not self.safety.check_emergency_stop():

            self.state_machine.emergency()

            return

        # -----------------------------
        # Conveyor Running?
        # -----------------------------

        if not self.conveyor.is_running():

            self.state_machine.stop()

            return

        self.state_machine.start()

        # -----------------------------
        # Wait Box
        # -----------------------------

        if not self.conveyor.has_box():

            if self.state_machine.get_state() != MachineState.WAIT_FOR_BOX:

                self.state_machine.wait_box()

            return

        # -----------------------------
        # Current Box
        # -----------------------------

        box = self.conveyor.get_current_box()

        self.state_machine.detect_box()

        if self.dashboard:

            self.dashboard.current_box.config(
                text=f"CURRENT : {box.color} | {box.size}"
            )

            self.dashboard.canvas.itemconfig(
                self.dashboard.box_item,
                fill="red" if box.color == "RED" else "blue"
            )

            self.dashboard.canvas.coords(
                self.dashboard.box_item,
                40,
                55,
                75,
                80
            )

            # Conveyor Travel

            while True:

                x1, y1, x2, y2 = self.dashboard.canvas.coords(
                    self.dashboard.box_item
                )

                if x1 >= 780:
                    break

                self.dashboard.canvas.move(
                    self.dashboard.box_item,
                    6,
                    0
                )

                self.dashboard.canvas.update()

                time.sleep(0.02)

            # Presence Sensor

            self.dashboard.canvas.itemconfig(
                self.dashboard.presence_led,
                fill="lime"
            )

            self.dashboard.sensor_presence_lbl.config(
                text="Presence : ON",
                fg="lime"
            )

            # Color Sensor

            self.dashboard.canvas.itemconfig(
                self.dashboard.color_led,
                fill="lime"
            )

            self.dashboard.sensor_color_lbl.config(
                text=f"Color : {box.color}",
                fg="lime"
            )

        # -----------------------------
        # Sensors
        # -----------------------------

        if not self.inputs.box_present(box):

            return

        color = self.inputs.read_color(box)

        size = self.inputs.read_size(box)

        print("\n========== BOX ==========")
        print("ID :", box.id)
        print("COLOR :", color)
        print("SIZE :", size)
        print("=========================")

        self.state_machine.sort_box()

        time.sleep(0.3)

        if color == "RED":

            self.outputs.push_left(box)

            if self.dashboard:

                self.dashboard.sort_lbl.config(
                    text="Sorting LEFT",
                    fg="red"
                )

                for i in range(8):

                    self.dashboard.canvas.move(
                        self.dashboard.left_pusher,
                        5,
                        0
                    )

                    self.dashboard.canvas.update()

                    time.sleep(0.02)

                for i in range(8):

                    self.dashboard.canvas.move(
                        self.dashboard.left_pusher,
                        -5,
                        0
                    )

                    self.dashboard.canvas.update()

                    time.sleep(0.02)

                self.animate_box(
                    980,
                    40
                )

        elif color == "BLUE":

            self.outputs.push_right(box)

            if self.dashboard:

                self.dashboard.sort_lbl.config(
                    text="Sorting RIGHT",
                    fg="cyan"
                )

                for i in range(8):

                    self.dashboard.canvas.move(
                        self.dashboard.right_pusher,
                        5,
                        0
                    )

                    self.dashboard.canvas.update()

                    time.sleep(0.02)

                for i in range(8):

                    self.dashboard.canvas.move(
                        self.dashboard.right_pusher,
                        -5,
                        0
                    )

                    self.dashboard.canvas.update()

                    time.sleep(0.02)

                self.animate_box(
                    980,
                    125
                )

            else:

                return

        # -----------------------------
        # Remove Box
        # -----------------------------

        self.state_machine.remove_box()

        self.conveyor.remove_box()

        if self.dashboard:

            self.dashboard.reset_visuals()

        self.state_machine.start()

    # =====================================================

    def animate_box(
        self,
        target_x,
        target_y
    ):

        canvas = self.dashboard.canvas

        # Move Right

        while True:

            x1, y1, x2, y2 = canvas.coords(
                self.dashboard.box_item
            )

            if x1 >= target_x:
                break

            canvas.move(
                self.dashboard.box_item,
                6,
                0
            )

            canvas.update()

            time.sleep(0.02)

        # Move Up / Down

        while True:

            x1, y1, x2, y2 = canvas.coords(
                self.dashboard.box_item
            )

            if abs(y1 - target_y) <= 3:
                break

            if y1 > target_y:

                canvas.move(
                    self.dashboard.box_item,
                    0,
                    -4
                )

            else:

                canvas.move(
                    self.dashboard.box_item,
                    0,
                    4
                )

            canvas.update()

            time.sleep(0.02)

    # =====================================================

    def connect_dashboard(
        self,
        dashboard
    ):

        self.dashboard = dashboard

    # =====================================================

    def run_scan(self):

        self.execute_cycle()
