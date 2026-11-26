import pytest
from nav import distance_m, bearing_deg


def test_same_point_is_zero():
    assert distance_m(27.45, -80.32, 27.45, -80.32) == 0


def test_one_degree_latitude():
    # 1 degree north-south is about 111,195 meters anywhere on Earth
    assert distance_m(0, 0, 1, 0) == pytest.approx(111195, rel=0.001)


def test_order_does_not_matter():
    a = distance_m(27.45, -80.32, 27.46, -80.30)
    b = distance_m(27.46, -80.30, 27.45, -80.32)
    assert a == pytest.approx(b)

def test_bearing_north():
    assert bearing_deg(0, 0, 1, 0) == pytest.approx(0)


def test_bearing_east():
    assert bearing_deg(0, 0, 0, 1) == pytest.approx(90)


def test_bearing_south():
    assert bearing_deg(0, 0, -1, 0) == pytest.approx(180)


def test_bearing_west():
    assert bearing_deg(0, 0, 0, -1) == pytest.approx(270)
