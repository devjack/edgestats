from pprint import pprint
from cloudfront_log_parser import parse
from io import BytesIO
from gzip import GzipFile
import boto3


class EdgeStats:
    def __init__(self):
        pass

    def process(log_contents):
        # This parses an AWS cloudfront log format.
        # Assumes log_contents is a huge string representing
        #  the whole .gz file, unzipped.
        pprint(len(log_contents))

class Metric:

    def __init__(self):
        self._dimensions = {}

    def set_dimensions(self, name, callback=callable):
        self._dimensions[name] = callback



# period: 1h
# dimensions:
#     - domain:function_name_to_produce_it()
#     - ip
#     - etc...
#
#
# 2017-10-01:10xxx developerjack.com 1.2.3.4 14
# 2017-10-01:10xxx developerjack.com 1.2.3.5 15
