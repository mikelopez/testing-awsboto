import sys
sys.path.append('../')
from local_settings import BUCKET_JOB_PICKUP, BUCKET_JOB_DONE, BUCKET_THUMBNAILS, \
						   MP4_PRESET_ID, TRANSCODER_PIPELINE
from common import *
from termprint import *
from random import randint
import unittest
import boto.elastictranscoder


INPUT_CONFIG = {
    'FrameRate': 'auto',
    'Resolution': 'auto',
    'AspectRatio': 'auto',
    'Interlaced': 'auto',
    'Container': 'auto'
}
MP4_OUTPUT = {
    'PresetId': MP4_PRESET_ID,
    'Rotate': '0', # dont rotate
    
}


class TestAWSConnection(unittest.TestCase):
    """Testing the Connection to AWS EC2"""
    
    def test_create_job(self):
        """Tests create_job to Transcoder"""
        et = boto.elastictranscoder.connect_to_region('us-east-1')
        #termprint('INFO', dir(ec))
        printobj(et)
        termprint('INFO', et.list_pipelines())
        INPUT_CONFIG['Key'] = 'samplevideo.mp4'
        MP4_OUTPUT['Key'] = 'rendered-%s.mp4' % (randint(111,9999))
        response = et.create_job(
        	TRANSCODER_PIPELINE,
        	INPUT_CONFIG,
        	MP4_OUTPUT,
        )

        termprint('INFO', dict(response))




if __name__ == '__main__':
    unittest.main()
