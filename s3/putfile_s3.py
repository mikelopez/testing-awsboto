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

        k = boto.s3.key.Key(bucket)
        k.key = 'testvideo.mp4'
        k.set_contents_from_filename('../testvideo.mp4')

        # allow some time
        time.sleep(2)
        for i in bucket.list():
            print i.name



if __name__ == '__main__':
    unittest.main()
