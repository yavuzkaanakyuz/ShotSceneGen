#!/usr/bin/env python3
"""
Setup script for text_to_shots package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="text_to_shots",
    version="1.0.0",
    author="Yavuz Kaan Akyuz",
    author_email="your-email@example.com",
    description="AI-powered package to convert text stories into film scenes and shots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yavuzkaanakyuz/ShotSceneGen",
    project_urls={
        "Bug Tracker": "https://github.com/yavuzkaanakyuz/ShotSceneGen/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
        ]
    },
    include_package_data=True,
)