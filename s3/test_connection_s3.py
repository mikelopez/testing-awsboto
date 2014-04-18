import sys
sys.path.append('../')
from common import *
from termprint import *
import unittest
import boto


class TestAWSConnection(unittest.TestCase):
    """Testing the Connection to AWS S3"""

    def test_s3connect(self):
        """Tests connection to S3"""
        s3 = boto.connect_s3()
        self.assertTrue(s3)
        printobj(s3)
        
        buckets_list = s3.get_all_buckets()


if __name__ == '__main__':
    unittest.main()
