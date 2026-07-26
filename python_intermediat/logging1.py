"""
What is Logging?
Logging is the process of recording information about what your program is doing.

| Level      | Purpose                                            |
| ---------- | -------------------------------------------------- |
| `DEBUG`    | Detailed information for developers                |
| `INFO`     | General program information                        |
| `WARNING`  | Something unexpected, but the program can continue |
| `ERROR`    | An operation failed                                |
| `CRITICAL` | Very serious error; the program may stop           |

"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s-%(asctime)s:%(message)s"
    )


logger = logging.getLogger("user logies:")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

fromatter = logging.Formatter("%(levelname)s-%(asctime)s:%(message)s")
handler.setFormatter(fromatter)

logger.addHandler(handler)

logger.info("a new user prformad a task ()")
logger.debug("debugging a module ..")
logger.critical("only 23 md ram left")
