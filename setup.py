"""Setup"""

from setuptools import setup, find_packages
from sodigest.version import VERSION

setup(
    name='sodigest',
    version=VERSION,
    description='Get a StackOverflow digest',
    url='https://github.com/trstringer/stackoverflow-digest',
    author='Thomas Stringer',
    author_email='github@trstringer.com',
    license='MIT',
    install_requires=['requests', 'PyYAML'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['sodigest=sodigest.main:main']
    )
)
