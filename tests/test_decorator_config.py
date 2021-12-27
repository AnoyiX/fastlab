import os
from fastlab.decorators import WithEnvConfig


@WithEnvConfig(prefix='FL_')
def load_config():
    return {'name': 'fastlab', 'version': '0.2.0'}


os.environ['FL_VERSION'] = '0.2.1'


conf = load_config()
assert conf == {'name': 'fastlab', 'version': '0.2.1'}
