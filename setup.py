from pathlib import Path

from setuptools import setup

setup(
    name="rokugu",
    version="0.0.3",
    description="An opinionated PySide6 library that delivers ready-to-use components and utilities.",
    long_description=Path("README.md").read_text("UTF-8"),
    long_description_content_type="text/markdown",
    author="Santos Vilanculos",
    author_email="santosvilanculos@yahoo.com",
    url="https://santosvilanculos.github.io/rokugu",
    project_urls={
        "Repository": "https://github.com/SantosVilanculos/rokugu",
        "Bug Tracker": "https://github.com/SantosVilanculos/rokugu/issues",
    },
    license="MIT",
    license_files=["LICENSE"],
    keywords=["PySide6"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.12,<3.14",
    requires=["setuptools", "wheel"],
    install_requires=[
        "pendulum>=3.0.0",
        "psutil>=7.0.0",
        "PySide6>=6.8.2.1",
    ],
)
