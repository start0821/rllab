# setup.py
from setuptools import find_packages, setup

setup(
    name='rllab',
    version='0.1.0',
    author='OpenAI',
    description='A framework for developing and evaluating reinforcement '
    'learning algorithms, fully compatible with OpenAI Gym',
    url='https://github.com/openai/rllab',
    packages=find_packages(
        '.',
        exclude=('contrib/', 'examples/', 'sandbox/', 'scripts/', 'tests/')),
    dependency_links=[
        # note that pip install requires --process-dependency-links!
        'git+https://github.com/Theano/Theano.git@adfe319ce6b781083d8dc3200fb4481b00853791#egg=Theano-0.9.0dev1',
        'git+https://github.com/neocxi/Lasagne.git@484866cf8b38d878e92d521be445968531646bb8#egg=Lasagne-0.2.dev1'
    ],
    install_requires=[
        # TODO: figure out which of these are truly necessary. Also split them
        # into install/dev dependencies.
        'numpy>=1.11',
        'scipy',
        'path.py',
        'python-dateutil',
        'joblib==0.9.4',
        # 'mako',
        # 'ipywidgets',
        # 'numba',
        # 'flask',
        # 'pybox2d',
        # 'pygame',
        'h5py',
        'matplotlib',
        # 'opencv3=3.1.0',
        'scikit-learn',
        # 'pytorch',
        # 'torchvision',
        'Pillow',
        # 'atari-py',
        'pyprind',
        # 'ipdb',
        # 'boto3',
        # 'PyOpenGL',
        # 'nose2',
        'pyzmq',
        'msgpack-python',
        # 'mujoco_py',
        'cached_property',
        'line_profiler',
        'cloudpickle',
        'Theano==0.9.0dev1',
        'Lasagne==0.2.dev1',
        # 'Cython',
        # 'redis',
        # 'git+https://github.com/Theano/Theano.git@adfe319ce6b781083d8dc3200fb4481b00853791#egg=Theano',
        # 'git+https://github.com/neocxi/Lasagne.git@484866cf8b38d878e92d521be445968531646bb8#egg=Lasagne',
        # 'git+https://github.com/plotly/plotly.py.git@2594076e29584ede2d09f2aa40a8a195b3f3fc66#egg=plotly',
        # 'awscli',
        # 'git+https://github.com/openai/gym.git@385a85fd0c1b26ab1374f208fbb370e22647548d#egg=gym',
        # 'pyglet',
        # 'git+https://github.com/neocxi/prettytensor.git',
        # 'jupyter',
        'progressbar2',
        # 'chainer==1.18.0',
        # 'tensorflow>=1.0'
    ],
    zip_safe=False)
