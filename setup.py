from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys
import os

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

class InstallDataset(install):
    def run(self):
        install.run(self)
        subprocess.check_call([sys.executable, 'corkit/dataset.py'])

version = '1.0.9'

def find_calibration_files():
    module_root = os.path.dirname(__file__)
    calibration_data_dir = os.path.join(module_root, 'corkit', 'data')
    calibration_files = []
    for root, _, files in os.walk(calibration_data_dir):
        for file in files:
            calibration_files.append(os.path.relpath(os.path.join(root, file), module_root))
    return calibration_files

if __name__ == '__main__':
    setup(
        name='corkit',
        version=version,
        packages=find_packages(),
        author='Jorge David Enciso Martínez',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author_email='jorged.encyso@gmail.com',
        description='Open source coronagraph data downloader and calibrator',
        url='https://github.com/Jorgedavyd/corkit',
        license='MIT',
        install_requires=[
            'astropy',
            'numpy',
            'aiofiles',
            'scipy',
            'scikit-image',
            'beautifulsoup4',
            'matplotlib',
            'pillow',
            'pandas',
        ],
        cmdclass={
            'install': InstallDataset
        },
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
            "Operating System :: MacOS :: MacOS X",
            "Topic :: Scientific/Engineering :: Astronomy",
            "Topic :: Scientific/Engineering :: Physics",
            "Topic :: Scientific/Engineering :: Visualization",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Framework :: Matplotlib",
            "Framework :: Pytest",
            "Framework :: Sphinx",
            "Framework :: Jupyter",
            "Framework :: IPython",
            "Environment :: Console",
            "Environment :: Web Environment",
            "Natural Language :: English",
            "Typing :: Typed",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Mathematics",
            "Topic :: Scientific/Engineering :: Information Analysis",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Coronagraph",
            "Topic :: Solar Physics",
            "Topic :: Astrophysics",
        ],
    )



