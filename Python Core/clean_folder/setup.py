from setuptools import setup, find_packages


setup(
    name='clean_folder',
    version='1.0',
    description='Clean your folder',
    url='https://github.com/OksanaDonchuk/goit-python/blob/main/clean.py',
    author='Oksana Donchuk',
    author_email='ksunya.donchuk@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)
