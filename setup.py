from setuptools import find_packages, setup

setup(
    name="jinnylab",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'shading_correction = jinnylab.shading_correction.cli:cli',
        ],
    },
)