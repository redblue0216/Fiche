from setuptools import setup,find_packages

setup(
        ### 包与作者信息
        name = 'fiche',
        version = '0.1',
        author = 'shihua',
        author_email = "hua.shi@meritech-data.com",
        python_requires = ">=3.9.12",
        license = "MIT",

        ### 源码与依赖
        packages = find_packages(),
        include_package_data = True,
        description = 'Fiche is a metadata management tool with MongoDB about algorithm info,model info,parameter info,application info,dataset info and more;supporting http interface and python sdk.',
        # install_requires = ['click','fastapi','rich','pymongo'],

        ### 包接入点，命令行索引
        entry_points = {
            'console_scripts': [
                'fichectl = fiche.cli:fiche'
            ]
        }      
)