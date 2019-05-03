#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fd:
    long_description = fd.read().strip()


with open("requirements.txt", "r") as fd:
    reqs = fd.read().splitlines()


setup(
    name='aura',
    version='0.1a1',
    description='Security aura for packages',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Martin Carnogursky',
    author_email='xcarnog@fi.muni.cz',
    url='https://github.com/RootLUG/aura',
    packages=['aura'],
    install_requires = reqs,
    entry_points = {
        'console_scripts': [
            'aura = aura.cli:main',
            'apip = aura.apip:main'
        ],
        'aura.analyzers': [
            'sensitive_files = aura.analyzers.fs_struct:analyze_sensitive',
            'suspicious_files = aura.analyzers.fs_struct:analyze_suspicious',
            'yara = aura.analyzers.yara_scan:analyze',
            'execution_flow = aura.analyzers.python.execution_flow:ExecutionFlow',
            'setup_py = aura.analyzers.setup:SetupPy',
            'data_finder = aura.analyzers.data_finder:DataFinder',
            'wheel = aura.analyzers.wheel:analyze_wheel'
        ],
        'aura.uri_handlers': [
            'pypi = aura.uri_handlers.pypi:PyPiHandler',
            'mirror = aura.uri_handlers.mirror:MirrorHandler',
            'local = aura.uri_handlers.local:LocalFileHandler'
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    zip_safe=False
)
