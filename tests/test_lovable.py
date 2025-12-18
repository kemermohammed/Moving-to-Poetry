from kattis.lovable import make_lvable


def test_lvable_already_contains_lv():
    # Only strings that literally have "lv"
    assert make_lvable("olv") == 0
    assert make_lvable("xlv") == 0


def test_lvable_one_change_needed():
    # Needs one operation → returns 1
    assert make_lvable("abcd") == 1
    assert make_lvable("vlxyz") == 1
    assert make_lvable("lvx") == 0  # already contains lv, edge case
    assert make_lvable("lxxxxv") == 1  # can form lv by replacing x


def test_lvable_edge_cases():
    # Very short strings
    assert make_lvable("l") == 1
    assert make_lvable("v") == 1
    assert make_lvable("") == 1
