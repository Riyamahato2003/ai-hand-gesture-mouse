# Check Installation

import pkg_resources

required_packages = {'numpy', 'opencv-python', 'tensorflow', 'flask'}
installed_packages = {pkg.key for pkg in pkg_resources.working_set}

if not required_packages.issubset(installed_packages):
    print("Some packages are missing!")
else:
    print("All required packages are installed.")