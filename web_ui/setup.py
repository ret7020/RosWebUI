from setuptools import setup

package_name = 'web_ui'
submodules = "web_ui/submodules"
setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name, submodules],
    package_data={package_name: ['templates/*.html', 'static/ros_wrapper.js', 'static/api.js']},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stephan',
    maintainer_email='ret7020@gmail.com',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'web_ui = web_ui.webui:main'
        ],
    },
)
