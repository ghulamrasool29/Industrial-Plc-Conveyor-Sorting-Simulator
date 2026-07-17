"""
dashboard.py
Industrial PLC HMI Dashboard
PART 1 / 4
Replace everything in dashboard.py with this first.
DO NOT keep old code.
"""
import tkinter as tk
from tkinter import messagebox
from random import choice
from datetime import datetime
import time

from conveyor.box import Box


class Dashboard:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Industrial PLC Conveyor Sorting System"
        )

        self.root.geometry("1250x600")
        self.root.resizable(False, False)

        # ---------------------------------

        self.bg = "#0f172a"
        self.panel = "#1e293b"
        self.header = "#111827"
        self.border = "#334155"

        self.root.configure(bg=self.bg)

        # ---------------------------------

        self.conveyor = None
        self.inputs = None
        self.outputs = None
        self.safety = None
        self.ladder = None
        self.state_machine = None

        self.start_time = time.time()

        # ==========================================
        # HEADER
        # ==========================================

        self.header_frame = tk.Frame(
            root,
            bg=self.header,
            height=60
        )

        self.header_frame.pack(
            fill="x"
        )

        tk.Label(
            self.header_frame,
            text="PLC CONVEYOR SORTING SIMULATOR",
            bg=self.header,
            fg="white",
            font=("Arial",20,"bold")
        ).pack(
            side="left",
            padx=20,
            pady=12
        )

        self.runtime_lbl = tk.Label(
            self.header_frame,
            text="Runtime : 00:00:00",
            bg=self.header,
            fg="#22c55e",
            font=("Arial",12,"bold")
        )

        self.runtime_lbl.pack(
            side="right",
            padx=20
        )

        # ==========================================
        # STATUS
        # ==========================================

        self.status_frame = tk.Frame(
            root,
            bg=self.bg
        )

        self.status_frame.pack(
            fill="x",
            pady=8
        )

        def status_box(title):

            frame = tk.Frame(
                self.status_frame,
                bg=self.panel,
                width=180,
                height=55,
                highlightbackground=self.border,
                highlightthickness=2
            )

            frame.pack_propagate(False)

            frame.pack(
                side="left",
                padx=8
            )

            lbl = tk.Label(
                frame,
                text=title,
                bg=self.panel,
                fg="white",
                font=("Arial",11,"bold")
            )

            lbl.pack(expand=True)

            return lbl

        self.state_lbl = status_box(
            "STATE : IDLE"
        )

        self.motor_lbl = status_box(
            "MOTOR : OFF"
        )

        self.total_box_lbl = status_box(
            "BOXES : 0"
        )

        self.processed_lbl = status_box(
            "PROCESSED : 0"
        )

        self.current_box = status_box(
            "CURRENT : NONE"
        )

        # ==========================================
        # CONVEYOR CANVAS
        # ==========================================

        self.canvas = tk.Canvas(

            root,

            width=1120,

            height=135,

            bg="#d6d6d6",

            highlightthickness=0

        )

        self.canvas.pack(
            pady=8
        )

        # Conveyor

        self.canvas.create_rectangle(

            40,

            50,

            900,

            85,

            fill="#4b5563",

            outline="black",

            width=2

        )

        self.rollers = []

        for x in range(50,890,25):

            line = self.canvas.create_line(

                x,

                50,

                x,

                85,

                fill="#1f2937",

                width=2

            )

            self.rollers.append(line)

        self.canvas.create_text(

            470,

            25,

            text="CONVEYOR BELT",

            font=("Arial",12,"bold")

        )

        # RED BIN

        self.canvas.create_rectangle(

            940,

            20,

            1100,

            65,

            fill="#dc2626",

            outline="black",

            width=2

        )

        self.canvas.create_text(

            1020,

            42,

            text="RED BIN",

            fill="white",

            font=("Arial",11,"bold")

        )

        # BLUE BIN

        self.canvas.create_rectangle(

            940,

            115,

            1100,

            160,

            fill="#2563eb",

            outline="black",

            width=2

        )

        self.canvas.create_text(

            1020,

            138,

            text="BLUE BIN",

            fill="white",

            font=("Arial",11,"bold")

        )

        # PUSHERS

        self.left_pusher = self.canvas.create_rectangle(

            820,

            52,

            845,

            70,

            fill="#94a3b8"

        )

        self.right_pusher = self.canvas.create_rectangle(

            820,

            110,

            845,

            128,

            fill="#94a3b8"

        )

        # MOVING BOX

        self.box_item = self.canvas.create_rectangle(

            -100,

            -100,

            -60,

            -60,

            fill="red",

            outline="black"

        )
        
        # ==========================================
        # SENSOR PANEL
        # ==========================================

        self.sensor_frame = tk.Frame(
            root,
            bg=self.bg
        )

        self.sensor_frame.pack(
            fill="x",
            pady=5
        )

        sensor_panel = tk.Frame(
            self.sensor_frame,
            bg=self.panel,
            highlightbackground=self.border,
            highlightthickness=2
        )

        sensor_panel.pack(
            side="left",
            padx=10
        )

        tk.Label(
            sensor_panel,
            text="SENSORS",
            bg=self.panel,
            fg="white",
            font=("Arial",12,"bold")
        ).pack(
            pady=5
        )

        sensor_canvas = tk.Canvas(
            sensor_panel,
            width=260,
            height=95,
            bg=self.panel,
            highlightthickness=0
        )

        sensor_canvas.pack()

        sensor_canvas.create_text(
            80,
            25,
            text="Presence",
            fill="white",
            font=("Arial",10)
        )

        self.presence_led = sensor_canvas.create_oval(
            150,
            15,
            170,
            35,
            fill="red"
        )

        sensor_canvas.create_text(
            80,
            65,
            text="Color",
            fill="white",
            font=("Arial",10)
        )

        self.color_led = sensor_canvas.create_oval(
            150,
            55,
            170,
            75,
            fill="red"
        )

        self.sensor_presence_lbl = tk.Label(
            sensor_panel,
            text="Presence : OFF",
            bg=self.panel,
            fg="red",
            font=("Arial",10,"bold")
        )

        self.sensor_presence_lbl.pack()

        self.sensor_color_lbl = tk.Label(
            sensor_panel,
            text="Color Sensor : OFF",
            bg=self.panel,
            fg="red",
            font=("Arial",10,"bold")
        )

        self.sensor_color_lbl.pack(
            pady=(0,5)
        )

        # ==========================================
        # TOWER LIGHT
        # ==========================================

        light_panel = tk.Frame(
            self.sensor_frame,
            bg=self.panel,
            highlightbackground=self.border,
            highlightthickness=2
        )

        light_panel.pack(
            side="left",
            padx=10
        )

        tk.Label(
            light_panel,
            text="TOWER LIGHT",
            bg=self.panel,
            fg="white",
            font=("Arial",12,"bold")
        ).pack(
            pady=5
        )

        self.light_canvas = tk.Canvas(
            light_panel,
            width=80,
            height=110,
            bg=self.panel,
            highlightthickness=0
        )

        self.light_canvas.pack(
            padx=10,
            pady=5
        )

        self.red_light = self.light_canvas.create_oval(
            25,10,55,40,
            fill="#500000"
        )

        self.yellow_light = self.light_canvas.create_oval(
            25,45,55,75,
            fill="#4a4200"
        )

        self.green_light = self.light_canvas.create_oval(
            25,80,55,110,
            fill="#003300"
        )

        # ==========================================
        # SORTING STATUS
        # ==========================================

        info_panel = tk.Frame(
            self.sensor_frame,
            bg=self.panel,
            highlightbackground=self.border,
            highlightthickness=2
        )

        info_panel.pack(
            side="left",
            padx=10,
            fill="both",
            expand=True
        )

        tk.Label(
            info_panel,
            text="SORTING STATUS",
            bg=self.panel,
            fg="white",
            font=("Arial",12,"bold")
        ).pack(
            pady=5
        )

        self.sort_lbl = tk.Label(
            info_panel,
            text="Waiting...",
            bg=self.panel,
            fg="cyan",
            font=("Arial",13,"bold")
        )

        self.sort_lbl.pack()

        self.queue_lbl = tk.Label(
            info_panel,
            text="Queue : 0",
            bg=self.panel,
            fg="white",
            font=("Arial",11)
        )

        self.queue_lbl.pack(
            pady=3
        )

        self.mode_lbl = tk.Label(
            info_panel,
            text="Sorting Mode : COLOR",
            bg=self.panel,
            fg="#22c55e",
            font=("Arial",11,"bold")
        )

        self.mode_lbl.pack(
            pady=3
        )

        # ==========================================
        # CONTROL BUTTONS
        # ==========================================

        self.button_frame = tk.Frame(
            root,
            bg=self.bg
        )

        self.button_frame.pack(
            pady=10
        )

        def plc_button(text,color,cmd):

            return tk.Button(

                self.button_frame,

                text=text,

                bg=color,

                fg="white",

                width=16,

                height=2,

                font=("Arial",10,"bold"),

                command=cmd

            )

        plc_button(
            "START",
            "#16a34a",
            self.start_system
        ).grid(row=0,column=0,padx=5)

        plc_button(
            "STOP",
            "#dc2626",
            self.stop_system
        ).grid(row=0,column=1,padx=5)

        plc_button(
            "ADD BOX",
            "#2563eb",
            self.add_box
        ).grid(row=0,column=2,padx=5)

        plc_button(
            "RESET",
            "#f59e0b",
            self.reset_emergency
        ).grid(row=0,column=3,padx=5)

        plc_button(
            "EMERGENCY",
            "#991b1b",
            self.emergency
        ).grid(row=0,column=4,padx=5)
        
        # ==========================================
        # EVENT LOG
        # ==========================================

        log_frame = tk.Frame(
            root,
            bg=self.bg
        )

        log_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(5,10)
        )

        tk.Label(
            log_frame,
            text="EVENT LOG",
            bg=self.bg,
            fg="white",
            font=("Arial",12,"bold")
        ).pack(
            anchor="w"
        )

        self.log = tk.Text(
            log_frame,
            bg="#111827",
            fg="#22c55e",
            font=("Consolas",10),
            height=10,
            insertbackground="white"
        )

        self.log.pack(
            fill="both",
            expand=True
        )

        # ==========================================
        # START TIMERS
        # ==========================================

        self.animate_belt()
        self.update_dashboard()

    # =====================================================

    def connect(
        self,
        conveyor,
        inputs,
        outputs,
        safety,
        ladder,
        state_machine
    ):

        self.conveyor = conveyor
        self.inputs = inputs
        self.outputs = outputs
        self.safety = safety
        self.ladder = ladder
        self.state_machine = state_machine

    # =====================================================

    def write_log(self, text):

        now = datetime.now().strftime("%H:%M:%S")

        self.log.insert(
            tk.END,
            f"[{now}] {text}\n"
        )

        self.log.see(tk.END)

    # =====================================================

    def animate_belt(self):

        if self.outputs and self.outputs.motor:

            for roller in self.rollers:

                self.canvas.move(
                    roller,
                    2,
                    0
                )

                x1, y1, x2, y2 = self.canvas.coords(roller)

                if x1 > 900:

                    self.canvas.coords(
                        roller,
                        50,
                        50,
                        50,
                        85
                    )

        self.root.after(
            50,
            self.animate_belt
        )

    # =====================================================

    def animate_box(self, target_x, target_y):

        while True:

            x1, y1, x2, y2 = self.canvas.coords(
                self.box_item
            )

            if x1 >= target_x:
                break

            dx = 5

            if y1 < target_y:
                dy = 2
            elif y1 > target_y:
                dy = -2
            else:
                dy = 0

            self.canvas.move(
                self.box_item,
                dx,
                dy
            )

            self.canvas.update()

            time.sleep(0.01)

    # =====================================================

    def update_dashboard(self):

        if self.state_machine:

            self.state_lbl.config(
                text=f"STATE : {self.state_machine.get_state().name}"
            )

        if self.outputs:

            if self.outputs.motor:

                self.motor_lbl.config(
                    text="MOTOR : ON"
                )

                self.light_canvas.itemconfig(
                    self.green_light,
                    fill="lime"
                )

            else:

                self.motor_lbl.config(
                    text="MOTOR : OFF"
                )

                self.light_canvas.itemconfig(
                    self.green_light,
                    fill="#003300"
                )

            if self.outputs.alarm:

                self.light_canvas.itemconfig(
                    self.red_light,
                    fill="red"
                )

            else:

                self.light_canvas.itemconfig(
                    self.red_light,
                    fill="#500000"
                )

        if self.conveyor:

            self.total_box_lbl.config(
                text=f"BOXES : {self.conveyor.count()}"
            )

            self.queue_lbl.config(
                text=f"Queue : {self.conveyor.count()}"
            )

            self.processed_lbl.config(
                text=f"PROCESSED : {self.conveyor.total_processed}"
            )

        runtime = int(
            time.time() - self.start_time
        )

        h = runtime // 3600
        m = (runtime % 3600) // 60
        s = runtime % 60

        self.runtime_lbl.config(
            text=f"Runtime : {h:02}:{m:02}:{s:02}"
        )

        if self.conveyor and self.conveyor.is_running():

            self.ladder.run_scan()

        self.root.after(
            300,
            self.update_dashboard
        )

    # =====================================================

    def start_system(self):

        self.inputs.press_start()

        self.outputs.motor_on()

        self.conveyor.start()

        self.sort_lbl.config(
            text="System Running...",
            fg="#22c55e"
        )

        self.write_log(
            "Machine Started"
        )

    # =====================================================

    def stop_system(self):

        self.inputs.press_stop()

        self.outputs.motor_off()

        self.conveyor.stop()

        self.state_machine.stop()

        self.sort_lbl.config(
            text="System Stopped",
            fg="orange"
        )

        self.write_log(
            "Machine Stopped"
        )

    # =====================================================

    def add_box(self):

        color = choice(
            ["RED", "BLUE"]
        )

        size = choice(
            ["SMALL", "LARGE"]
        )

        box = Box(
            color,
            size
        )

        self.conveyor.add_box(
            box
        )

        self.current_box.config(
            text=f"CURRENT : {color} | {size}"
        )

        self.canvas.coords(
            self.box_item,
            45,
            73,
            75,
            103
        )

        self.canvas.itemconfig(
            self.box_item,
            fill="red" if color == "RED" else "blue"
        )

        self.sensor_presence_lbl.config(
            text="Presence : ON",
            fg="lime"
        )

        self.canvas.itemconfig(
            self.presence_led,
            fill="lime"
        )

        self.write_log(
            f"Added Box -> {color} | {size}"
        )

    # =====================================================

    def emergency(self):

        self.inputs.press_emergency()

        self.outputs.alarm_on()

        self.sort_lbl.config(
            text="!!! EMERGENCY !!!",
            fg="red"
        )

        self.write_log(
            "Emergency Stop Activated"
        )

        messagebox.showwarning(
            "Emergency",
            "Emergency Stop Activated!"
        )

    # =====================================================

    def reset_emergency(self):

        self.safety.reset_emergency()

        self.outputs.alarm_off()

        self.sort_lbl.config(
            text="Emergency Reset",
            fg="#22c55e"
        )

        self.write_log(
            "Emergency Reset"
        )

    # =====================================================

    def reset_visuals(self):

        self.canvas.coords(
            self.box_item,
            -100,
            -100,
            -60,
            -60
        )

        self.canvas.itemconfig(
            self.presence_led,
            fill="red"
        )

        self.canvas.itemconfig(
            self.color_led,
            fill="red"
        )

        self.canvas.itemconfig(
            self.left_pusher,
            fill="#94a3b8"
        )

        self.canvas.itemconfig(
            self.right_pusher,
            fill="#94a3b8"
        )

        self.sensor_presence_lbl.config(
            text="Presence : OFF",
            fg="red"
        )

        self.sensor_color_lbl.config(
            text="Color Sensor : OFF",
            fg="red"
        )

        self.current_box.config(
            text="CURRENT : NONE"
        )

        self.sort_lbl.config(
            text="Waiting...",
            fg="cyan"
        )