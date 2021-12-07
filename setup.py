# -*- coding: utf-8 -*-
"""
Codon2Vec metdata Library
@author: RWint
"""

from setuptools import setup 
from setuptools import find_packages

setup(
      name='Codon2Vec',
      version='1.0',
      description='A neural network tool for classifying and predicting expression of protein-coding sequences based on codon usage.',
      author='Rhondene Wint',
      author_email='rwint@ucmerced.edu',
      url='https://github.com/rhondene/Codon2Vec',
      license='MIT',
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience:: Research Scientists',
                   'License:: OSI Approved:: MIT License'],
      keywords="codon usage, bioinformatics, machine learning",
      packages=find_packages(),
      install_requires=['Keras==2.3.0',
                        'matplotlib==3.4.2',
                        'numpy==1.17.2',
                        'pandas==1.0.5',
                        'scikit-learn==0.24.2',
                        'scipy==1.3.1',
                        'seaborn==0.11.0',
                        'tensorflow==2.0.0']
      )