from setuptools import setup, find_packages

requires = [
    'spotipy',
    'flask',
    'requests',
    'requests_html',
    'pathlib',
    'pandas'
]

setup(
    name='demo',
    packages = find_packages(),
    include_package_data = True,
    install_requires = requires
)
