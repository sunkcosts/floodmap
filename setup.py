from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="floodmap",
    version="0.0.2",
    author="Hart Traveller",
    url="https://github.com/sunkcosts/floodmap",
    license="MIT",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click", "requests"],
    entry_points={"console_scripts": ["floodmap=floodmap.cli:entry"]},
)
