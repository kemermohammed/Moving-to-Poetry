from kattis.twoques import faster_queue


def test_queue_left_faster():
    left_times = [1, 2, 3]
    right_times = [2, 3, 5]
    assert faster_queue(left_times, right_times) == "left"


def test_queue_right_faster():
    left_times = [4, 4]
    right_times = [3, 2]
    assert faster_queue(left_times, right_times) == "right"


def test_queue_equal():
    left_times = [1, 2, 3]
    right_times = [2, 3, 1]
    assert faster_queue(left_times, right_times) == "either"


def test_queue_empty_lists():
    left_times = []
    right_times = []
    # Both queues empty → sums equal → either
    assert faster_queue(left_times, right_times) == "either"
