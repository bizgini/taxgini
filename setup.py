from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="taxgini",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["frappe"],
    description="Custom Tax Gini App for Frappe/ERPNext",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="BizGini",
    license="MIT",
)
