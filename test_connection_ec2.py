import sys
sys.path.append('../')
from common import *
from termprint import *
import unittest
import boto.ec2

class TestAWSConnection(unittest.TestCase):
    """Testing the Connection to AWS EC2"""

    def test_ec2connect(self):
        """Tests connection to EC2"""
        ec = boto.ec2.connect_to_region('us-east-1')
        printobj(ec)


if __name__ == '__main__':
    unittest.main()
