from distutils.core import setup
setup(
    name = 'PostProcess',
    version='0.1dev',
    author='Y. Jeong',
    author_email='youngung.jeong@gmail.com',
    scripts=['shellsort.f', 'cmp.py'],
#    packages=['myfirstpack','myfirstpack.test'],
#    package_dir={'myfirstpack':'myfirstpack'},
#    scripts=['bin/ex01.py']
#    license='LICENSE.txt',
    description='Aggregate of various python scripts for post-processing',
    long_description=open('README').read(),
#    install_requires=[
#        'gfortran >= 4.6',
#        'matplotlib >= 1.3',
#        'numpy >= 1.8'],
    )
