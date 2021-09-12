from toyrobot.point import Point


def test_add_point_positive_test_case():
    point_obj_1 = Point(0, 0)
    point_obj_2 = Point(1, 1)
    result = point_obj_1 + point_obj_2
    assert point_obj_2.x_co_ordinate == result.x_co_ordinate
    assert point_obj_2.y_co_ordinate == result.y_co_ordinate


def test_add_point_negative_test_case():
    point_obj_1 = Point(0, 0)
    point_obj_2 = Point(1, 1)
    result = point_obj_1 + point_obj_2
    assert point_obj_1.x_co_ordinate != result.x_co_ordinate
    assert point_obj_1.y_co_ordinate != result.y_co_ordinate


def test_gt_point_positive_test_case():
    point_obj_1 = Point(0, 0)
    point_obj_2 = Point(1, 1)
    result = point_obj_2 >= point_obj_1
    assert result == True


def test_gt_point_negative_test_case():
    point_obj_1 = Point(0, 0)
    point_obj_2 = Point(1, 1)
    result = point_obj_1 >= point_obj_2
    assert result == False


def test_lt_point_positive_test_case():
    point_obj_1 = Point(0, 0)
    point_obj_2 = Point(1, 1)
    result = point_obj_1 <= point_obj_2
    assert result == True


def test_lt_point_negative_test_case():
    point_obj_1 = Point(0, 0)
    point_obj_2 = Point(1, 1)
    result = point_obj_2 <= point_obj_1
    assert result == False
