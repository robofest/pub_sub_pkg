import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'pub_sub_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # This line includes all launch files during colcon build:
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yml]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cchung',
    maintainer_email='cchung@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
	        'pub_node_exe = pub_sub_pkg.pub_node:main',
            'sub_node_exe = pub_sub_pkg.sub_node:main',
        ],
    },
)