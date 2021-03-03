import re
import setuptools


with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

with open("discord/ext/converters/__init__.py", "r") as stream:
    version = re.search(r"^version = [\"]([^\"]*)[\"]", stream.read(), re.MULTILINE).group(1)

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

project_urls = {
    "Issue Tracker": "https://github.com/Ext-Creators/discord-ext-converters/issues",
    "Source": "https://github.com/Ext-Creators/discord-ext-converters",
}

setuptools.setup(
    author="Ext-Creators",
    classifiers=classifiers,
    description="A discord.py extension with a collection of useful converters.",
    install_requires=install_requires,
    license="Apache Software License",
    name="discord-ext-converters",
    packages=["discord.ext.converters", "discord.ext.converters.custom_converters"],
    project_urls=project_urls,
    python_requires=">=3.6.0",
    url="https://github.com/Ext-Creators/discord-ext-converters",
    version=version,
)
