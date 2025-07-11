from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="ipagent",
    version="0.1.6",
    description="FastAPI dependency: get client IP device browser and geo data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Musharraf Ibragimov",
    author_email="meibrohimov@email.com",
    url="https://github.com/allncuz/ipagent",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    install_requires=[
        "fastapi>=0.100",
        "httpx>=0.24.0",
        "user-agents>=2.2.0",
        "pydantic>=2.11.7"
    ],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    ],
)
