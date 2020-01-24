from setuptools import setup, find_packages

setup(
    name='cli',
    version=open('VERSION').read().strip(),
    #version=__version__,
    author='Francesco De Carlo',
    author_email='decarlof@gmail.com',
    url='https://github.com/decarlof/cli',
    packages=find_packages(),
    include_package_data = True,
    scripts=['bin/cli'],
    description='cli',
    zip_safe=False,
)

