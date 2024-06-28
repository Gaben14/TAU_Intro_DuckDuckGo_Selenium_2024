import logging
import datetime as dt

DRIVER_FOR_SCRSHOOT = None

# class LogSearch:

def log_details():
    # Logging
    # Get the logger and set its level
    today = dt.datetime.today()
    now = dt.datetime.now()

    log_filename = f"{today.month:02d}-{today.day:02d}-{today.year}.log"

    logger = logging.getLogger("searchLog")
    logger.setLevel(logging.ERROR)

    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f"logs/{log_filename}")

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s"
    )

    # Add the formatter to the handlers:
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    DRIVER_FOR_SCRSHOOT.save_screenshot(f"logs/{today.month:02d}-"
                                 f"{today.day:02d}-{today.year}-"
                                 f"{now.hour:02d}-{now.minute:02d}-"
                                 f"{now.second:02d}.png")

    return logger