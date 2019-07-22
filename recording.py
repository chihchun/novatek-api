#!/usr/bin/python
from novatek import Novatek
import time

N = Novatek()

while True:
  try:
    sec = N.get_recording_sec()
    if sec > 0:
      print("Stop system recording. (%s)" % sec)  
      N.stop_record()
    else:
      print("Start system recording. (%s)" % sec)  
      N.start_record()

    break
  except requests.exceptions.ConnectionError:
    pass
  except KeyboardInterrupt:
    sys.exit(1)
  except Exception:
    logging.exception('Unhandled exception while waiting for camera')
    raise

  time.sleep(1.0)
