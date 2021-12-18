from fastlab import logs

# Python3 Logging
# See more: https://docs.python.org/3/library/logging.html

logs.warning('warn')    # 2021-12-18 14:23:31.000  WARNING 88493 --- [  MainThread] test_logs        : warn
logs.info('info')       # 2021-12-18 14:23:31.000     INFO 88493 --- [  MainThread] test_logs        : info
logs.error('error')     # 2021-12-18 14:23:31.000    ERROR 88493 --- [  MainThread] test_logs        : error
