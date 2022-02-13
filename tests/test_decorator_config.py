import os
from fastlab.decorators import WithEnvConfig


@WithEnvConfig(prefix='FL_')
def load_config():
    return {
        'name': 'fastlab',
        'version': '0.2.1',
        'extra': {
            'memory_lock': False
        }
    }


os.environ['FL_VERSION'] = '0.0.0'
os.environ['FL_EXTRA_MEMORY__LOCK'] = 'true'


conf = load_config()
assert conf == {
    'name': 'fastlab',
    'version': '0.0.0',
    'extra': {
        'memory_lock': True
    }
}
