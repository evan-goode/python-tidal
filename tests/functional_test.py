import unittest
from tidalapi4mopidy import *


class MyTestCase(unittest.TestCase):
    def test_lossless_url(self):
        s = Session(Config(quality=Quality.lossless))
        s.login('', '')
        url = s.get_media_url(track_id=36336294)
        print(url)
        self.assertRegex(url, '\.flac', msg='Encrypted stream?')

    def test_hq_url(self):
        s = Session(Config(quality=Quality.high))
        s.login('', '')
        url = s.get_media_url(track_id=36336294)
        print(url)
        self.assertRegex(url, '\.m4a', msg='Encrypted stream?')


if __name__ == '__main__':
    unittest.main()
