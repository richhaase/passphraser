from setuptools import setup

setup(
    name = "passphraser",
    version = "0.0.1",
    author = "Rich Haase",
    author_email = "richh@posteo.net",
    description = ("A simple diceware based passphrase generator"),
    license = "GPLv3+",
    keywords = "diceware passphrase password security",
    url="https://github.com/richhaase/passphraser",
    packages=["passphraser", "tests"],
    classifiers=[
        "Developent Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
)
