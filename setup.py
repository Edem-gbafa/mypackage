from setuptools import setup, find_packages

setup(
    name ='mypackage',
    version = '0.1',
    packages = find_packages(exclude=['test*']),
    license='MIT',
    description='EDSA my first Python pagckage',
    long_description=open('README.md').read(),
    install_requires =['numpy'],
    url='https://github.com /<Edem-Gbafa>/<mypackage>',
    author='<Edem Gbafa>',
    author_email='<bells.edem@gmail.com>'
)