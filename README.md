# EdgeStats

EdgeStats is an analytics tool for AWS CloudFront access logs.

[![Build Status](https://travis-ci.org/devjack/edgestats.svg?branch=master)](https://travis-ci.org/devjack/edgestats)

## Getting Started

EdgeStats requires a few setup steps:

1) Checkout the project
2) Setup your zappa_settings.json file (sample provided)
2a) _Probably something about setting up dynamodb here_
3) `zappa deploy <env>`

Other useful commands:

To install package from source: `pip install -e .`
To install w/ dev dependencies: `pip install -e ".[dev]"`


## Running the tests

Quite straightforward:

```
python setup.py test
```

And for linting (assumes pylint is available or you've installed .[dev] above)

```
pylint
```

## Sample config:

EdgeStats assumes you are able to provide the contents of an AWS CloudFront log
The simplest case is to load from S3 once the log is written. A sample is
 provided in the samples/ directory.

Test cases load sample data from tests/data/* files (all are gzipped)

## Deployment

To publish a new version of edgestats:
 * Bump the versions in `setup.py`
 * Ensure your local ~/.pypirc file is configured

First ensure:

```
pip install wheel twine
rm  -rf dist/*          # A clean dist directory
```

And then:

```
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*
```


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on the code of conduct and how to submit bugs. Pull requests would also be wonderful!

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/devjack/edgestats/tags).

## Authors

* **Jack Skinner** - *Founder* - [@developerjack](https://twitter.com/developerjack)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
