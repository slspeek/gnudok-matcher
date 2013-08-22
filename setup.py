from setuptools import setup, find_packages

setup(
    name = "matcher",
    version = "1.0",
    url = 'http://code.google.com/p/gnudok-matcher/',
    license = 'GPL',
    description = "matcher for Juttersdok",
    author = 'Steven Speek',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools',
                        'factory_boy==1.2.0',
                        'docutils',
                        'flup==1.0.2',
                        'django-bootstrap-toolkit',
                        'django==1.4.2',
                        'django-nose',
                        'django-webtest',
                        'WebTest', 
                        'django_jenkins',
                        'selenium',
                        'South',
                        'MySQL-python'],
)
