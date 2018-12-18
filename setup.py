import os
import sys

from setuptools import setup

readme = 'README.md'
if os.path.exists('README.rst'):
    readme = 'README.rst'
with open(readme) as f:
    long_description = f.read()


def build_native(spec):
    # build an example rust library
    build = spec.add_external_build(
        cmd=['cargo', 'build', '--release'],
        path='.'
    )

    spec.add_cffi_module(
        module_path='is_minified_js._native',
        dylib=lambda: build.find_dylib('is_minified_js', in_path='target/release'),
        header_filename=lambda: build.find_header('is_minified_js.h', in_path='.'),
        rtld_flags=['NOW', 'NODELETE']
    )


setup(
    name='is-minified-js',
    version='0.3.0',
    description='Detecting minified javascript files',
    long_description=long_description,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Rust',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
    ],
    author='Messense Lv',
    author_email='messense@icloud.com',
    packages=['is_minified_js'],
    setup_requires=['milksnake'],
    install_requires=['cffi'],
    milksnake_tasks=[
        build_native
    ],
    include_package_data=True,
    zip_safe=False,
)
