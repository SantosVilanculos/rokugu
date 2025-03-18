from pathlib import Path

from setuptools import setup

setup(
    name="rokugu",
    version="0.0.1",
    description="An opinionated PySide6 library that delivers ready-to-use components and utilities.",
    long_description=Path("README.md").read_text("UTF-8"),
    long_description_content_type="text/markdown",
    author="Santos Vilanculos",
    author_email="santosvilanculos@yahoo.com",
    url="http://github.com/SantosVilanculos/rokugu",
    license="MIT",
    keywords=["Qt6", "PySide6"],
    package_dir={"": "src"},
    python_requires=">=3.12",
    requires=["setuptools", "wheel"],
    install_requires=[
        "pendulum",
        "pillow",
        "psutil",
        "PySide6",
    ],
)
