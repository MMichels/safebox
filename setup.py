import os
from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize


sources = ["./safebox/safebox.pyx"]
includes = []
for root, folder, files in os.walk("./safebox/src"):
    for file in files:
        if file.endswith("cpp"):
            sources.append(os.path.join(root, file))
    includes.append(root)



extensions = [
    Extension(
        name="safebox",
        sources=sources,
        include_dirs=includes,
        define_macros=[
            ("PRIVATE_KEY", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
            ("PRIVATE_IV", "bbbbbbbbbbbbbbbb")            
        ]
    )
]

setup(
    name="safebox",
    version="1.0",
    description="A safe waay to store your Python application credetials",
    long_description="""This application is build with cython and c/c++ code, this allow us to store a \"super secret key\" to encrypt and decrypt strings, this allow to store, with a minimum safety, crypted strings, this strings, can be, for ex. users, passwords, address to database connection.
    IMPORTANT: This module comes with random keys, but is EXTREMALLY RECOMENDED than you compile this module by you own, from sources, to define YOUR UNIQUE secret key on the c/c++ modules.
    IMPORTANT2: The PRIVATE_KEY must be 32bytes long (32 chars) and the PRIVATE_IV must be 16bytes long.    
    """,
    author="Mateus Michels de Oliveira",
    author_email="michels09@hotmail.com",
    ext_modules=cythonize(extensions),
    requires=["setuptools", "wheel", "Cython"],
    packages=find_packages()
)