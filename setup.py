from setuptools import setup, find_packages

setup(
    name='ai_shell_framework',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    author='Mounish',
    description='AI-driven terminal shell framework for intelligent OS',
    long_description=open('docs/AI_Shell_Framework_Complete.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YOUR_USERNAME/ai_os_shell_framework',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)