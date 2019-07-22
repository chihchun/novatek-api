#!/usr/bin/python
from novatek import Novatek
import time
N = Novatek()

while True:
  try:
    print("System responsed %d" % N.ping())
    print("Firmware version %s" % N.firmware_version())

    break
  except KeyboardInterrupt:
    sys.exit(1)
  except Exception:
    raise
  time.sleep(3.0)
