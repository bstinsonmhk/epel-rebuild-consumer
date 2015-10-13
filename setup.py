from setuptools import setup

setup(
    name='epelrebuild',
    version='0.0.1',
    description='',
    author='',
    author_email='',
    url='',
    install_requires=["fedmsg"],
    packages=[],
    entry_points={
        'moksha.consumer': (
            'epelrebuild = epelrebuild:EpelRebuild',
        ),
    },
)
