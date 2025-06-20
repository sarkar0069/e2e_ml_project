from setuptools import find_packages,setup

hypen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup (
    name = 'e2e_ml_project',
    version = '0.0.1',
    author='arpan',
    author_email='arpansarkar2468@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)