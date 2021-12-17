import logging

logs = logging.getLogger('console')
logs.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
log_format = '%(asctime)s %(levelname)+8s %(process)d --- [%(threadName)+12s] %(module)-16s : %(message)s'
formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S.000')
handler.setFormatter(formatter)
logs.addHandler(handler)
