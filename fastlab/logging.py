import logging

logs = logging.getLogger('console')
logs.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
log_format = '%(asctime)s.%(msecs)03d %(levelname)+8s %(process)d --- [%(threadName)+12s] %(module)-16s : %(message)s'
formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logs.addHandler(handler)
