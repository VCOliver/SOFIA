# dummy_gpio.py
class dummyGPIO(object):
    BCM = "BCM_MODE"
    BOARD = "BOARD_MODE"
    OUT = "OUT"
    IN = "IN"
    LOW = 0
    HIGH = 1
    
    verbose = False

    def __init__(self):
        self.pin_states = {}  # Track pin states
        self.mode = None

    def setmode(self, mode):
        self.mode = mode
        if self.verbose:
            print "[DUMMY GPIO] Set mode: %s" % mode

    def setup(self, pin, mode, initial=None):
        self.pin_states[pin] = {
            "mode": mode,
            "state": initial if initial is not None else self.LOW
        }
        if self.verbose:
            print "[DUMMY GPIO] Setup pin %d as %s (initial=%s)" % (pin, mode, initial)

    def output(self, pin, state):
        if pin in self.pin_states:
            self.pin_states[pin]["state"] = state
            if self.verbose:
                print "[DUMMY GPIO] Pin %d set to %s" % (pin, state)
        else:
            if self.verbose:
                print "[DUMMY GPIO] Pin %d not initialized!" % pin

    def cleanup(self):
        self.pin_states = {}
        print "[DUMMY GPIO] Cleanup"

    def setwarnings(self, flag):
        if self.verbose:
            print "[DUMMY GPIO] Warnings %s" % ("enabled" if flag else "disabled")
        
        
import random

class dummyADS1115(object):
    def __init__(self):
        self.gain = 1
        self.voltage = 12.0  # Simulated baseline voltage
        self.current = 1.5   # Simulated baseline current
        self.temp = 25.0     # Simulated baseline temperature

    def read_adc(self, channel, gain=1):
        # Simulate sensor noise (0.1)
        noise = random.uniform(-0.1, 0.1)
        
        if channel == 0:  # Voltage channel
            raw_value = (self.voltage + noise) * 1000  # Simulate ADC scaling
        elif channel == 1:  # Current channel
            raw_value = (self.current + noise) * 1000
        elif channel == 2:  # Temperature channel
            # Reverse of temp formula: temp = 0.0044*raw - 6.216
            raw_value = (self.temp + noise + 6.216) / 0.0044
        else:
            raw_value = 0
            
        return int(raw_value)

    def set_voltage(self, voltage):
        """For testing: Manually set voltage"""
        self.voltage = voltage

    def set_current(self, current):
        """For testing: Manually set current"""
        self.current = current

    def set_temp(self, temp):
        """For testing: Manually set temperature"""
        self.temp = temp
