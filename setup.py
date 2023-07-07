from setuptools import setup, find_packages

setup(
    name='MIDI_Controller_App',
    version='1.0',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'midi_controller_app = src.main:main',
        ],
    },
    package_data={
        '': ['*.txt', '*.md'],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Windows application to detect MIDI information from external MIDI controllers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/midi_controller_app',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.8',
    ],
)