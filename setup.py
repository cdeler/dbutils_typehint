from setuptools import setup

setup(
        name='dbutils_typehint',
        version='0.1.9',
        packages=['dbutils_typehint'],
        url='https://github.com/cdeler/dbutils_typehint',
        license='MIT',
        author='cdeler',
        author_email='serj.krotov@gmail.com',
        description='Provides type hints for dbutils in Data Bricks: '
                    'https://docs.databricks.com/dev-tools/databricks-utils.html',
        python_requires='>=3.5',
)
