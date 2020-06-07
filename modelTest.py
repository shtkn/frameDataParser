import unittest
import StringIO
from model import *

class TestModel(unittest.TestCase):

    def test_combine_2_wait_frames(self):
        chunks = [WaitFrames(2), WaitFrames(4)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrames(6)]
        self.assertItemsEqual(expected, result)

    def test_combine_2_active_frames(self):
        chunks = [ActiveFrames(2), ActiveFrames(2, is_new_hit=False)]
        result = consolidate_frame_chunks(chunks)
        expected = [ActiveFrames(4)]
        self.assertItemsEqual(expected, result)

    def test_dont_combine_2_active_frames(self):
        chunks = [ActiveFrames(2, is_new_hit=True), ActiveFrames(2, is_new_hit=True)]
        result = consolidate_frame_chunks(chunks)
        expected = [ActiveFrames(2), ActiveFrames(2)]
        self.assertItemsEqual(expected, result)

    def test_combine_2_wait_frames_with_active_after(self):
        chunks = [WaitFrames(2), WaitFrames(4), ActiveFrames(1), WaitFrames(2)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrames(6), ActiveFrames(1), WaitFrames(2)]
        self.assertItemsEqual(expected, result)

    def test_do_not_combine_wait_frames_with_inv(self):
        chunks = [WaitFrames(2), WaitFrames(4)]
        chunks[0].inv_type = 0
        chunks[1].inv_type = 1
        result = consolidate_frame_chunks(chunks)
        expected = chunks
        self.assertItemsEqual(expected, result)

    def test_do_not_combine_wait_frames_with_diff_inv(self):
        chunks = [WaitFrames(2), WaitFrames(2)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, True, True, True, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, False, False, False, False]
        result = consolidate_frame_chunks(chunks)
        expected = chunks
        self.assertItemsEqual(result, expected)

    def test_do_combine_wait_frames_with_diff_inv(self):
        chunks = [WaitFrames(2), WaitFrames(2)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, True, True, True, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, False, False, False, False]
        result = consolidate_frame_chunks(chunks, True)
        expected = [WaitFrames(4)]
        self.assertEqual(len(expected), len(result))
        self.assertEqual(expected[0].duration, result[0].duration)  # inv for this combined chunk is undefined behavior

    def test_do_not_combine_active_frame_types_with_same_inv(self):
        chunks = [ActiveFrames(2, is_new_hit=True), ActiveFrames(2, is_new_hit=True)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [True, False, False, False, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, False, False, False, False]
        result = consolidate_frame_chunks(chunks)
        expected = chunks
        self.assertItemsEqual(result, expected)

    def test_combine_active_frame_types_with_same_inv(self):
        chunks = [ActiveFrames(2, is_new_hit=True), ActiveFrames(2, is_new_hit=False)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, False, False, False, True]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [False, False, False, False, True]
        result = consolidate_frame_chunks(chunks)
        expected = [ActiveFrames(4)]
        expected[0].inv_type = 1
        expected[0].inv_attr = [False, False, False, False, True]
        self.assertItemsEqual(result, expected)

    def test_combine_same_frame_types_with_same_inv(self):
        chunks = [WaitFrames(2), WaitFrames(4)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, True, True, True, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [False, True, True, True, False]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrames(6)]
        expected[0].inv_type = 1
        expected[0].inv_attr = [False, True, True, True, False]
        self.assertItemsEqual(result, expected)
