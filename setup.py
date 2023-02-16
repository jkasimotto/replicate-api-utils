from setuptools import setup, find_packages

setup(
    name='replicate_api_utils',
    version='0.1.0',
    author='Your Name',
    description='Python package for accessing the Replicate API',
    packages=find_packages(),
    install_requires=[
        'click',
        'replicate',
        # any other necessary dependencies
    ],
)
