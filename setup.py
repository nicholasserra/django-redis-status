from setuptools import setup, find_packages

setup(
    name='django-redis-status',
    version='1.1.0',
    description='A django application that displays some statistics about your redis instance in the admin.',
    long_description=open('README.md').read(),
    author='Nicholas Serra',
    author_email='nickserra@gmail.com',
    url='https://github.com/nicholasserra/django-redis-status',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
