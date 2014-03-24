import sys
sys.path.append('../')
from common import *
from termprint import *
from random import randint
import unittest
import boto
import time

testbucket = "test-nodelete"

class TestS3Read(unittest.TestCase):
    """Testing reading Connection to S3 and create/delete a bucket"""
    
    def test_s3shit(self):
        s3 = boto.connect_s3()
        bucket = s3.get_bucket(testbucket)
        self.assertTrue(bucket)

        termprint('INFO', ' %s' % bucket.list())
        bl = bucket.list()
        termprint('ERROR', bl)
        for i in bl:
            print i.name


if __name__ == '__main__':
    unittest.main()
