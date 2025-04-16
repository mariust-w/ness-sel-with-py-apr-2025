import logging

# debug,info,warning,error,critical

logging.basicConfig(filename="ness.log", format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Debug message")
logger.info("Just an information")
logger.warning("it's a warning")
logger.error("Did you try to divide the number by zero")
logger.critical("Network issue")