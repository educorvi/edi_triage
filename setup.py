from setuptools import setup, find_packages

setup(
    name='edi-triage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        # e.g., 'requests >= 2.25.1',
    ],
    # Metadata
    author='Jonas Hüttinger',
    author_email='jonas.huettinger@educorvi.de',
    description='A package for examine files on a very low level for triage.',
    keywords='educorvi, edi, triage, converter',
    url='https://github.com/educorvi/edi_triage.git',  # Project home page
)
