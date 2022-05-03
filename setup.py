import datetime
import os, sys
from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize


DEFAULT_PK = "f2b403ea764d11eb94390242ac130002"
DEFAULT_IV = "76fc77c44a46c70a"


PRIVATE_KEY = os.getenv("PRIVATE_KEY", DEFAULT_PK)
PRIVATE_IV =  os.getenv("PRIVATE_IV", DEFAULT_IV)

default_values = PRIVATE_KEY == DEFAULT_PK or PRIVATE_IV == DEFAULT_IV
print("PRIVATE_KEY: {}\nPRIVATE_IV: {}\n".format(PRIVATE_KEY, PRIVATE_IV))
if default_values:
    print(
        "!!!ATTENTION!!! YOU ARE USING THE DEFAULT PRIVATE AND IV KEYS, "
        +"WHATs IS NOT!!! A FULL SAFE POLICY, "
        +"LEARN MORE ON: https://github.com/MMichels/safebox")



sources = ["./safebox/safebox.pyx"]
includes = []
for root, folder, files in os.walk("./safebox/src"):
    for file in files:
        if file.endswith("cpp"):
            sources.append(os.path.join(root, file))
    includes.append(root)

long_description = ""
with open("README.MD") as f:
    long_description = f.read()


extensions = [
    Extension(
        name="safebox",
        sources=sources,
        include_dirs=includes,
        define_macros=[
            ("PRIVATE_KEY", PRIVATE_KEY),
            ("PRIVATE_IV", PRIVATE_IV)            
        ]
    )
]


setup(
    name="safebox",
    version=datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
    description="A safe waay to store your Python application credetials",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Mateus Michels de Oliveira",
    author_email="michels09@hotmail.com",
    ext_modules=cythonize(extensions),
    requires=["setuptools", "wheel", "Cython"],
    packages=find_packages(),
    url="https://github.com/MMichels/safebox"
)