import setuptools
from pathlib import Path

directory = Path(__file__).parent
readme = (directory/"README.md").read_text()

setuptools.setup(
        name="zhcode",
        version="0.0.5",
        author="lnjng",
        description="Programming languages in Chinese.",
        license='MIT',
        long_description=readme,
        long_description_content_type='text/markdown',
        url='https://github.com/Injng/zhcode',
        packages=["zhcode", "zhcode.python"]
        )
