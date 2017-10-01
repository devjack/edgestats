from setuptools import setup, find_packages

setup(
    name="edgestats",
    description='Cloudscale analytics for cloudfront access logs',
    license="MIT",
    version='0.0.1',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['cloudfront', 'analytics'],
    install_requires=[
        'boto3',
        'cloudfront-log-parser',
        'cloudfront-edge-codes',
    ],
    extras_require={
        'dev': [
            'pylint',
        ]
    },
    python_requires='~=3.6',
    entry_points = {
        # 'console_scripts': ['endpointer=endpointer.cli:cli'],
    },
    test_suite="tests",
)
