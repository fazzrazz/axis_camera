import os
from glob import glob
from setuptools import setup

package_name = 'axis_camera'

setup(
    name=package_name,
    version='0.4.3',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.py')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Chris Iverach-Brereton',
    maintainer_email='civerachb@clearpathrobotics.com',
    description='Python ROS 2 drivers for accessing an Axis camera\'s MJPG stream. Also provides control for PTZ cameras.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'resource = lrs_exec.resource:main'
        ]
    }
    
)
