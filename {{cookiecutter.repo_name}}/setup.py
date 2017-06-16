import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

with open('requirements.txt') as reqs:
    required = reqs.read().splitlines()

with open('dev_requirements.txt') as dev_reqs:
    dev_required = dev_reqs.read().splitlines()

    class PyTest(TestCommand):
        user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='{{cookiecutter.project_name}}',
    short_description="{{cookiecutter.project_short_description}}",
    version='0.1',
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    packages=['{{cookiecutter.repo_name}}'],
    package_dir={'{{cookiecutter.repo_name}}': '{{cookiecutter.repo_name}}'},
    include_package_data=True,
    install_requires=required,
    classifiers=(
        'Development Status :: 3 - Alpha'
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ),
    cmdclass={'test': PyTest},
    tests_require=dev_required
)
