import sys
sys.path.append('../')
from common import *
from termprint import *
from random import randint
import unittest
import boto

import time

testbucket = "test-nodelete"

class TestS3KeyExists(unittest.TestCase):
        
    def test_s3_file_exists(self):
        """Tests to see if a file exists"""
        s3 = boto.connect_s3()
        bucket = s3.get_bucket(testbucket)
        self.assertTrue(bucket)
        k = bucket.get_key('testvideo.mp4')
        termprint('INFO', k)
        termprint('ERROR', k.__dict__)
        termprint('INFO', 'Found %s' % k.name)



if __name__ == '__main__':
    unittest.main()
