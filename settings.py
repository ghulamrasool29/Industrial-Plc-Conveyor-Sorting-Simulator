"""
Project 4
PLC Based Conveyor Sorting System

Global Configuration File
"""

# -----------------------------
# Conveyor Settings
# -----------------------------

CONVEYOR_SPEED = 1.0          # meter/sec (simulation)
BOX_TRAVEL_TIME = 3           # seconds to reach sorting point

# -----------------------------
# Sensor Delay
# -----------------------------

SENSOR_DELAY = 0.5            # seconds

# -----------------------------
# Pneumatic Pusher Timing
# -----------------------------

PUSHER_ACTIVE_TIME = 1.0      # seconds

# -----------------------------
# Alarm
# -----------------------------

ALARM_DURATION = 2

# -----------------------------
# Safety
# -----------------------------

EMERGENCY_STOP_PRIORITY = True

# -----------------------------
# Box Types
# -----------------------------

BOX_COLORS = [
    "RED",
    "BLUE"
]

BOX_SIZES = [
    "SMALL",
    "LARGE"
]