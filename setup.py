from setuptools import find_packages, setup

setup(
    name='smartis_api',
    version='0.1',
    packages=find_packages(),
    description='Python wrapper for the Smartis API',
    author='Artem Samoilov',
    author_email='samoylovartem07@gmail.com',
    install_requires=[
        'requests',
        'pydantic',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
