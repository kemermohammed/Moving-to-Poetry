from kattis.real import fence_length
import math

def test_fence_basic():
    # Area 1 → 4*sqrt(1) = 4
    assert math.isclose(fence_length(1), 4.0, rel_tol=1e-9)

def test_fence_large_area():
    # Area 16 → 4*sqrt(16) = 16
    assert math.isclose(fence_length(16), 16.0, rel_tol=1e-9)

def test_fence_small_area():
    # Area 0.25 → 4*sqrt(0.25) = 2
    assert math.isclose(fence_length(0.25), 2.0, rel_tol=1e-9)

def test_fence_zero_area():
    # Area 0 → perimeter 0
    assert math.isclose(fence_length(0), 0.0, rel_tol=1e-9)
