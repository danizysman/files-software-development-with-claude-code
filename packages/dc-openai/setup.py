from setuptools import setup

setup(
    name="dc-openai",          # the package name (used by pip, can be anything)
    version="1.0.0",           # version string, bump it when you change the file
    py_modules=["dc_openai"],  # the filename WITHOUT .py — tells pip which file to install
    install_requires=["requests"],  # installs requests automatically as a dependency
    python_requires=">=3.6",   # documents the minimum Python version
)
