import sys
sys.path.append('../')
from common import *
from termprint import *
import unittest
import boto.elastictranscoder

class TestAWSConnection(unittest.TestCase):
    """Testing the Connection to AWS EC2"""
    
    def test_transcoderconnect(self):
        """Tests connection to Transcoder"""
        et = boto.elastictranscoder.connect_to_region('us-east-1')
        #termprint('INFO', dir(ec))
        printobj(et)
        termprint('INFO', et.list_pipelines())


if __name__ == '__main__':
    unittest.main()
