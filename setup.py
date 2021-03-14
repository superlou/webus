import setuptools


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='webus',
    version='0.1.0',
    description='Requirements document generation',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    packages=['webus'],
    entry_points={
        'console_scripts': ['webus=webus:command_line'],
    },
    python_requires='>=3.6',
)
