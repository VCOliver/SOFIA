# Legacy Monitoring and Control System

This project is a legacy monitoring and control system originally written in Python 2 using PyQt4. It was designed to interface with hardware (via ADCs, DACs, and GPIO) on a Raspberry Pi for monitoring parameters such as voltage, current, power, impedance, and temperature, while also logging calibration data to an Excel spreadsheet.

**Main Goals:**
- **Legacy Maintenance:** Maintain and run the existing Python 2 code for legacy systems.
- **Modernization:** Gradually refactor and update the codebase to a modern Python version (Python 3.11+) and newer libraries (e.g., PyQt5 or PySide6).

---

## Features

- **Graphical User Interface:** Built with PyQt4, featuring real-time displays and control buttons.
- **Data Logging:** Exports calibration and operational data to an Excel file using `xlwt`.
- **PID Control:** Implements a PID controller to adjust the system output based on sensor feedback.
- **Hardware Integration:** (Optional) Interfaces with ADCs, DACs, and relays (using RPi.GPIO, smbus, etc.) for physical systems.
- **Simulation Mode:** When running on a desktop (with `RPI_ON` set to `False`), the code can simulate ADC and DAC readings for development and testing.

---

## Prerequisites

### Legacy Environment (Python 2.7)
- **Python:** 2.7.x
- **Libraries:**
  - PyQt4
  - xlwt
  - NumPy
  - SciPy
  - Custom modules: `parametros`, `controller`, `PID`
- **Optional (for hardware integration):**
  - RPi.GPIO, smbus, and an ADC library (e.g., Adafruit_ADS1x15)

### Modernization Target (Python 3.11+)
- Update to **Python 3.11**.
- Consider migrating from PyQt4 to PyQt5 or PySide6.
- Update legacy libraries and refactor code as needed.

---

## Setting Up the Conda Environment

To recreate the environment on another machine:

```bash
conda env create -f environment.yml
conda activate <your_environment_name>
```
