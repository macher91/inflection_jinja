from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'jinja2>=2.10.1',
    'inflection>=0.3.1'
    ]

setup_requirements = []

test_requirements = []

setup(
    author="Mateusz Mejsner",
    author_email='mateusz.mejsner@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ],
    description="Jinja extension wrapping infection package.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='jinja_inflection',
    name='jinja_inflection',
    packages=find_packages(include=['jinja-inflection']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lesleslie/jinja-inflection',
    version='0.2.0',
    zip_safe=False,
    )
