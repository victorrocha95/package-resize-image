from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="resize_image",
    version="0.0.1",
    author="Victor Rocha",
    author_email="victorrocha.ti@gmail.com",
    description="Pacote simples em python para redimensionar uma imagem",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/victorrocha95/package-resize-image"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)