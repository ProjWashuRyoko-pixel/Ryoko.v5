# setup_enhanced.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="project-ryoko-enhanced",
    version="0.2.0",
    author="Project Ryoko Community",
    author_email="community@project-ryoko.org",
    description="An enhanced universal framework for modeling identity emergence in complex systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/project-ryoko/framework",
    packages=find_packages(include=['ryoko', 'ryoko.*']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Sociology",
        "Topic :: Education",
    ],
    python_requires=">=3.8",
    install_requires=requirements + [
        "numpy>=1.21.0",
        "pydantic>=1.9.0",  # For enhanced data validation
        "pyyaml>=6.0",      # For YAML configuration support
        "matplotlib>=3.5.0", # For visualization (optional)
        "pytest>=6.0",      # For testing
        "pytest-asyncio>=0.18.0",  # For async tests
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "pytest-asyncio>=0.18.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.910",
            "pre-commit>=2.15",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "sphinx-autodoc-typehints>=1.12",
        ],
        "viz": [
            "matplotlib>=3.5.0",
            "plotly>=5.5.0",
            "seaborn>=0.11.0",
        ],
        "ml": [
            "scikit-learn>=1.0.0",
            "torch>=1.9.0",
            "transformers>=4.10.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "ryoko-demo=ryoko.demo:main",
            "ryoko-viz=ryoko.visualization.cli:main [viz]",
            "ryoko-train=ryoko.training.cli:main [ml]",
        ],
    },
    include_package_data=True,
    package_data={
        "ryoko": ["configs/*.yaml", "configs/*.json"],
    },
)