#!/usr/bin/python
from novatek import Novatek
import datetime

N = Novatek()

while True:
  try:
    # N.ping()
    print(N.get_config())
    print(N.set_date(datetime.datetime.utcnow()))
    print(N.set_time(datetime.datetime.utcnow().time()))

    break
  except requests.exceptions.ConnectionError:
    pass
  except KeyboardInterrupt:
    sys.exit(1)
  except Exception:
    logging.exception('Unhandled exception while waiting for camera')
    raise
  time.sleep(1.0)
