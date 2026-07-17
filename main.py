"""
main.py

Industrial PLC Conveyor Sorting Simulator
Main Entry Point
"""

import tkinter as tk

from conveyor.conveyor import Conveyor

from plc.inputs import PLCInputs
from plc.outputs import PLCOutputs
from plc.safety import SafetySystem
from plc.state_machine import StateMachine
from plc.ladder_logic import LadderLogic

from ui.dashboard import Dashboard


def main():

    # ==========================================
    # Conveyor
    # ==========================================

    conveyor = Conveyor()

    # ==========================================
    # PLC Components
    # ==========================================

    plc_inputs = PLCInputs()

    plc_outputs = PLCOutputs()

    state_machine = StateMachine()

    safety = SafetySystem(
        plc_inputs,
        plc_outputs
    )

    ladder = LadderLogic(
        conveyor,
        plc_inputs,
        plc_outputs,
        safety,
        state_machine
    )

    # ==========================================
    # GUI
    # ==========================================

    root = tk.Tk()

    dashboard = Dashboard(root)

    dashboard.connect(
        conveyor=conveyor,
        inputs=plc_inputs,
        outputs=plc_outputs,
        safety=safety,
        ladder=ladder,
        state_machine=state_machine
    )
    
    ladder.connect_dashboard(dashboard)

    root.mainloop()


if __name__ == "__main__":
    main()