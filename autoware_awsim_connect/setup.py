## launch fileを実行する場合はコメントアウトを解除
from setuptools import find_packages, setup
## import os 
## from glob import glob

package_name = 'autoware_awsim_connect'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
       ## (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),  (launch)
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sato',
    maintainer_email='sato@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "simple_publish_node=autoware_awsim_connect.simple_publish_node:main",
            "velocity_subscribe_node=autoware_awsim_connect.velocity_subscribe_node:main",
            "steering_subscribe_node=autoware_awsim_connect.steering_subscribe_node:main",
            "control_mode_subscribe_node=autoware_awsim_connect.control_mode_subscribe_node:main",
            "gear_subscribe_node=autoware_awsim_connect.gear_subscribe_node:main",
            "turn_indicators_subscribe_node=autoware_awsim_connect.turn_indicators_subscribe_node:main",
            "hazard_lights_subscribe_node=autoware_awsim_connect.hazard_lights_subscribe_node:main",
            "control_publish_node=autoware_awsim_connect.control_publish_node:main", # publish
            "gear_publish_node=autoware_awsim_connect.gear_publish_node:main",
            "turn_indicators_publish_node=autoware_awsim_connect.turn_indicators_publish_node:main",
            "hazard_lights_publish_node=autoware_awsim_connect.hazard_lights_publish_node:main",
            "engage_publish_node=autoware_awsim_connect.engage_publish_node:main",
        ]
    },
)
