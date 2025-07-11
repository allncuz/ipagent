from setuptools import setup, find_packages

setup(
    name="ipagent",
    version="0.1.4",
    description="FastAPI dependency: get client IP, device, browser, and geo data",
    author="Musharraf Ibragimov",
    author_email="meibrohimov@email.com",
    url="https://github.com/allncuz/ipagent.git",
    packages=find_packages(),
    include_package_data=True,
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
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    ],
)
