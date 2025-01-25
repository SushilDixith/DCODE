from setuptools import setup, find_packages

setup(
    name="dcode",
    version="1.0.0",
    description="A native hashing tool using MD5, SHA-1, and SHA-256.",
    author="Sushil Dixith",
    author_email="sushildixith.s@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dcode=dcode.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

