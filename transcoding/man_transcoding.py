import sys
sys.path.append('../')
from common import *
from termprint import *
from random import randint
import unittest
import boto.elastictranscoder
try:
    import local_settings as settings
    BUCKET_JOB_DONE = getattr(settings, "BUCKET_JOB_DONE")
    BUCKET_JOB_PICKUP = getattr(settings, "BUCKET_JOB_PICKUP")
except:
    # get some default fallback values
    BUCKET_JOB_DONE = None
    BUCKET_JOB_PICKUP = None

BUCKET_THUMBNAILS = BUCKET_JOB_DONE
MP4_PRESET_ID = getattr(settings, "MP4_PRESET_ID")
TRANSCODER_PIPELINE = getattr(settings, "TRANSCODER_PIPELINE")

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

RUN = False

class TestAWSConnection(unittest.TestCase):
    """Testing the Connection to AWS EC2"""
    
    def test_create_job(self):
        """Tests create_job to Transcoder"""
        if RUN:
            et = boto.elastictranscoder.connect_to_region('us-east-1')
            #termprint('INFO', dir(ec))
            printobj(et)
            termprint('INFO', et.list_pipelines())
            for i in os.listdir('/home/ubuntu/downloaded_03312014/completed'):
                if '.mov' in i:
                    INPUT_CONFIG['Key'] = i
                    MP4_OUTPUT['Key'] = '%s-%s.mp4' % (i, randint(111,9999))
                    response = et.create_job(
                        TRANSCODER_PIPELINE,
                        INPUT_CONFIG,
                        MP4_OUTPUT,
                    )

                    termprint('INFO', dict(response))




if __name__ == '__main__':
    unittest.main()
