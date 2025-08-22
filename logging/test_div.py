import logging

logger2 = logging.getLogger(__name__)
logger2.setLevel(logging.INFO)

# configure the handler and formatter for logger2
handler2 = logging.FileHandler(f"{__name__}.log", mode='w')
formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# add formatter to the handler
handler2.setFormatter(formatter2)
# add handler to the logger
logger2.addHandler(handler2)

logger2.info(f"Testing the custom logger for module {__name__}...") 

def test_division(x,y):
    try:
        x/y
        logger2.info(f"x/y successful with result: {x/y}.")
    except ZeroDivisionError as err:
        logger2.exception("ZeroDivisionError")
