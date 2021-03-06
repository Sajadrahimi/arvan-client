import setuptools


version = "0.0.8"
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arvan_client",
    version=version,
    author="Sajad Rahimi",
    author_email="rahimisajad@outlook.com",
    description="A Python SDK for ArvanCloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sajadrahimi/arvan-client",
    project_urls={
        "Bug Tracker": "https://github.com/sajadrahimi/arvan-client/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"arvan_client": "arvan_client"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
