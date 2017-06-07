import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

try:
    from setuptools_rust import RustExtension
except ImportError:
    import subprocess
    errno = subprocess.call([sys.executable, '-m', 'pip', 'install', 'setuptools-rust'])
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)
    else:
        from setuptools_rust import RustExtension


class PyTest(TestCommand):
    user_options = []

    def run(self):
        self.run_command("test_rust")

        import subprocess
        import sys
        errno = subprocess.call([sys.executable, '-m', 'pytest', 'tests'])
        raise SystemExit(errno)


setup_requires = ['setuptools-rust>=0.6.0']
install_requires = []
tests_require = install_requires + ['pytest']


setup(
    name='is-minified-js',
    version='0.1.0',
    description='JSON',
    long_description='',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Rust',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Internet :: WWW/HTTP',
    ],
    author='Messense Lv',
    author_email='messense@icloud.com',
    packages=['is_minified_js'],
    rust_extensions=[RustExtension('is_minified_js._is_minified_js', 'Cargo.toml', pyo3=True, debug=False)],
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    include_package_data=True,
    zip_safe=False,
    cmdclass=dict(test=PyTest)
)
