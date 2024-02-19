from setuptools import setup

setup(
    name="pkg-manage",
    description="Testing package management using the packagekit-control snap interface",
    version="0.1",
    url="https://github.com/st3v3nmw/snap-test-packagekit",
    author="Stephen Mwangi",
    license="MIT",
    python_requires=">=3.10",
    packages=["pkg_manage"],
    entry_points={
        "console_scripts": ["pkg-manage=pkg_manage.main:main"],
    },
)
