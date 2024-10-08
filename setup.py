from setuptools import setup, find_packages

setup(
    name='diarization',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'simple-diarizer @ git+https://github.com/DamianoLozzi/simple_diarizer.git',
        'torchvision>=0.19.0',
        'speechbrain>=1.0.1',
        'soundfile>=0.12.1'
    ],
    description='A simple diarization package',
    author='DamianoLozzi',
    author_email='damianolozzi1989@gmail.com',
    url='',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)

        
