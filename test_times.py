import pytest

from times import compute_overlap_time, time_range


# 原有测试：一个大区间包含两个小区间
def test_generic_case():
    large = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 12:00:00",
    )
    short = time_range(
        "2010-01-12 10:30:00",
        "2010-01-12 10:45:00",
        2,
        60,
    )

    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]

    assert compute_overlap_time(large, short) == expected


# 新测试 1：两个时间范围完全不重叠
def test_no_overlap():
    range1 = time_range(
        "2010-01-12 09:00:00",
        "2010-01-12 10:00:00",
    )
    range2 = time_range(
        "2010-01-12 11:00:00",
        "2010-01-12 12:00:00",
    )

    expected = []

    assert compute_overlap_time(range1, range2) == expected


# 新测试 2：两个时间范围各自包含三个区间
def test_multiple_intervals():
    range1 = time_range(
        "2010-01-12 09:00:00",
        "2010-01-12 14:00:00",
        3,
        3600,
    )
    range2 = time_range(
        "2010-01-12 09:30:00",
        "2010-01-12 14:30:00",
        3,
        3600,
    )

    expected = [
        ("2010-01-12 09:30:00", "2010-01-12 10:00:00"),
        ("2010-01-12 11:30:00", "2010-01-12 12:00:00"),
        ("2010-01-12 13:30:00", "2010-01-12 14:00:00"),
    ]

    assert compute_overlap_time(range1, range2) == expected


# 新测试 3：一个区间结束时，另一个恰好开始
def test_touching_intervals():
    range1 = time_range(
        "2010-01-12 09:00:00",
        "2010-01-12 10:00:00",
    )
    range2 = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 11:00:00",
    )

    # 只有端点相接，没有正时长的重叠
    expected = []

    assert compute_overlap_time(range1, range2) == expected

def test_touching_intervals_2(): # 总共第五个function
        first_range = time_range(
            "2010-01-12 00:00:00",
            "2010-01-12 12:00:00",
        )
        second_range = time_range(
            "2010-01-12 12:00:00",
            "2010-01-13 00:00:00",
        )

        expected = [ ]

        result = compute_overlap_time(first_range, second_range)
        assert result == expected


def test_backwards_time_range():
    with pytest.raises(ValueError,
                       match="end_time must be greater than start_time"
                       ):
        time_range(
            "2010-01-12 12:00:00",
            "2010-01-12 09:00:00",
        )


#from times import compute_overlap_time, time_range # 从times.py中导入compute_overlap_time（计算两个时间的重叠部分）和time_range（准备时间范围）函数

# def test_generic_case():
    #large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    #short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    #expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    #assert compute_overlap_time(large, short) == expected 
    # 一个list 包含两个tuple 
    # 每个元组保存一个区间的开始和结束时间，格式是字符串
    # 调用函数，检查实际重叠结果是否与预期列表完全相等，直接比较结果，所以不用另写result=...

