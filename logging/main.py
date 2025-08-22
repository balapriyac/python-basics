import sentry_sdk

sentry_sdk.init(
     dsn="<your-dsn-key-here>",
     traces_sample_rate=0.85,
)

import logging
from test_div import test_division

# get a custom logger & set the logging level
py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

# configure the handler and formatter as needed
py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# add formatter to the handler
py_handler.setFormatter(py_formatter)
# add handler to the logger
py_logger.addHandler(py_handler)

py_logger.info(f"Testing the custom logger for module {__name__}...")

x_vals = [2,3,6,4,10]
y_vals = [5,7,12,0,1]

for x_val,y_val in zip(x_vals,y_vals):
    x,y = x_val, y_val
    # call test_division
    test_division(x,y)
    py_logger.info(f"Call test_division with args {x} and {y}")
