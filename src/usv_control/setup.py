import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'usv_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # ADD THIS NEW LINE BELOW:
        (os.path.join('share', package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amandeep',
    maintainer_email='amandeep@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'dummy_gps = usv_control.dummy_gps:main',
            'nav_brain = usv_control.nav_brain:main', 
            'motor_driver = usv_control.motor_driver:main',
        ],
    },
)
