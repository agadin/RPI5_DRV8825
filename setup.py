from setuptools import setup, find_packages

setup(
    name='RPI5_DRV8825',
    version='1.0.0',
    description='An updated DRV8825 stepper motor driver library for Raspberry Pi 5',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Alexandru Gadin',
    author_email='112425293+agadin@users.noreply.github.com',
    url='https://github.com/agadin/RPI5_DRV8825',
    packages=find_packages(),
    install_requires=[
        'lgpio',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Unlicense',
        'Operating System :: Raspbian',
    ],
    python_requires='>=3.6',
)