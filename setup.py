import setuptools

with open ("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__="0.0.0"
REPO_NAME = "Machine_learning_Ops_with_MLFlow"
AUTHOR_USER_NAME = "Kishan"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "kishanajudiya13@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="python package for ml app",
    long_description=long_description,
    long_description_content="text/markdwon",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)