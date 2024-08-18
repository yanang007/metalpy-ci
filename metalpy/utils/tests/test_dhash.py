import pathlib

import numpy as np
import pandas as pd

from metalpy.utils.dhash import dhash


def _dummy(x):
    return x + 225


def test_dhash_stable():
    """验证dhash的稳定性（在不同次运行中哈希结果一致）
    """
    dhash_records = [
        # Basic Python types
        (225,  7846919982185809875),
        (2.25,  -3918227367074148393),
        (2 + 25j,  -6412466123961202416),
        (True,  325184529882986853),
        (None,  -7934642784484250388),
        (b'225',  5436264356540408418),  # bytes
        ('0225',  6433453438383710489),

        # Python collections
        ((2, '2', 5.0), -5582375266051148848),
        ([2, '2', 5.0], -5582375266051148848),
        ({0: 2.0, np.int8(2): '5'},  1876027385350813336),

        # Python functions and classes
        (_dummy,  6449074981454838072),
        (int,  -5394466986204997707),

        # Numpy types
        (np.int8(25),  -5921789015889676150),
        (np.uint8(225),  7846919982185809875),
        (np.float32(225),  7846919982185809875),
        (np.int16(225),  7846919982185809875),
        (np.uint16(225),  7846919982185809875),
        (np.float64(225),  7846919982185809875),
        (np.intc(225),  7846919982185809875),
        (np.uintc(225),  7846919982185809875),
        (np.longdouble(225),  7846919982185809875),
        (np.int32(225),  7846919982185809875),
        (np.uint32(225),  7846919982185809875),
        (np.complex64(225),  7846919982185809875),
        (np.float16(225),  7846919982185809875),
        (np.int64(225),  7846919982185809875),
        (np.uint64(225),  7846919982185809875),
        (np.complex128(2 + 25j),  -6412466123961202416),
        (np.bool_(True),  325184529882986853),
        (np.array([2, 25]),  -5297488126673252258),

        # Numpy datetime types
        (np.datetime64('2021-12-25'),  -8803879579640539530),
        (np.timedelta64(5, 'D'),  3974400344764180608),

        # Pandas types
        (pd.Series([2, 25]),  -5297488126673252258),
    ]

    # Pathlib types
    try:
        dhash_records.append((pathlib.WindowsPath('C:\\Users'), 6348354964056181059))
    except NotImplementedError:
        dhash_records.append((pathlib.PosixPath('/home'), 1298416137799441881))

    for k, v in dhash_records:
        hashed = dhash(k)
        assert dhash(k) == v, f"Unexpected dhash result for {k}: got {hashed.result} (expected {v})"
