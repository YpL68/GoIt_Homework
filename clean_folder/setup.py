from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='First package',
      author='YpL',
      author_email='test@example.com',
      license='MIT',
      readme="README.md",
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      packages=find_namespace_packages(),
      include_package_data=True,
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:clean_folder']}
     )