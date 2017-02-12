import logging


log = logging.getLogger("buses")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())
