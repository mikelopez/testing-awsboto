import sys
sys.path.append('../')
from common import *
from termprint import *
from random import randint
import unittest
import boto
import time

class TestS3(unittest.TestCase):
    """Testing the Connection to S3 and create/delete a bucket"""

    def test_s3shit(self):
        # ehlo
        s3 = boto.connect_s3()
        bucket = s3.create_bucket('test-%s' % randint(1111,999999))

        # create keypair
        key = bucket.new_key('testkey')
        key.set_contents_from_string('Hello World')

        # output
        self.__output_bucket(bucket)
        self.__output_key(key)
        
        # relax man
        time.sleep(2)
        key.get_contents_as_string()
        key.delete()
        bucket.delete()

    def __output_bucket(self, data):
        # output
        termprint('ERROR', 'PRINT BUCKET')
        printobj(data)
    def __output_key(self, data):
        # output
        termprint('ERROR', 'PRINT KEY')
        printobj(data)

if __name__ == '__main__':
    unittest.main()
