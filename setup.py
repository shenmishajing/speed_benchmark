# coding:utf-8

from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="speed-benchmark",
    version="1.0.0",
    description="A generic speed benchmark library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="shenmishajing",
    author_email="shenmishajing@gmail.com",
    url="https://github.com/shenmishajing/speed_benchmark",
    project_urls={
        "Code": "https://github.com/shenmishajing/speed_benchmark",
        "Issue tracker": "https://github.com/shenmishajing/speed_benchmark/issues",
    },
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
    license="MIT License",
    packages=find_packages(),  # 包
    platforms=["all"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: GPU :: NVIDIA CUDA",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: Chinese (Simplified)",
    ],
)
