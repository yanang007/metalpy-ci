import numpy as np


class Bounds(np.ndarray):
    def __new__(cls, input_arr) -> 'Bounds':
        return np.asarray(input_arr).view(cls)

    def __array_finalize__(self, _, **__):
        pass

    def as_corners(self):
        """从边界形式转换为角落点形式

        Returns
        -------
        ret
            角落点形式表示的
        """
        return self.reshape(2, -1).T.view(Corners)

    def expand(self, proportion=None, increment=None, inplace=False):
        number = (int, float)
        deltas = np.tile(np.asarray((-1, 1)), self.n_axes)
        if increment is None:
            assert proportion is not None, 'Either `proportion` or `increment` must be provided.'
            if isinstance(proportion, number):
                proportion = deltas * proportion
            increment = self.extent.repeat(2) * proportion

        if isinstance(proportion, number):
            increment = increment * deltas

        if inplace:
            target = self
        else:
            target = self.copy()

        target += increment
        return target

    @property
    def extent(self):
        return self.end - self.origin

    @property
    def origin(self):
        return self[::2]

    @origin.setter
    def origin(self, val):
        self[::2] = val

    @property
    def end(self):
        return self[1::2]

    @end.setter
    def end(self, val):
        self[1::2] = val

    @property
    def xmin(self): return self[0]

    @xmin.setter
    def xmin(self, v): self[0] = v

    @property
    def xmax(self): return self[1]

    @xmax.setter
    def xmax(self, v): self[1] = v

    @property
    def ymin(self): return self[2]

    @ymin.setter
    def ymin(self, v): self[2] = v

    @property
    def ymax(self): return self[3]

    @ymax.setter
    def ymax(self, v): self[3] = v

    @property
    def zmin(self): return self[4]

    @zmin.setter
    def zmin(self, v): self[4] = v

    @property
    def zmax(self): return self[5]

    @zmax.setter
    def zmax(self, v): self[5] = v

    @property
    def n_axes(self): return self.shape[0] // 2


class Corners(np.ndarray):
    def __new__(cls, input_arr):
        return np.asarray(input_arr).view(cls)

    def __array_finalize__(self, _, **kwargs):
        pass

    def as_bounds(self):
        """从角落点形式转换为边界形式

        Returns
        -------
        ret
            角边界形式表示的
        """
        return self.T.ravel().view(Bounds)

    @property
    def extent(self):
        return self.end - self.origin

    @property
    def origin(self):
        return self[0]

    @origin.setter
    def origin(self, val):
        self[0] = val

    @property
    def end(self):
        return self[1]

    @end.setter
    def end(self, val):
        self[1] = val

    @property
    def xmin(self): return self[0, 0]

    @xmin.setter
    def xmin(self, v): self[0, 0] = v

    @property
    def xmax(self): return self[1, 0]

    @xmax.setter
    def xmax(self, v): self[1, 0] = v

    @property
    def ymin(self): return self[0, 1]

    @ymin.setter
    def ymin(self, v): self[0, 1] = v

    @property
    def ymax(self): return self[1, 1]

    @ymax.setter
    def ymax(self, v): self[1, 1] = v

    @property
    def zmin(self): return self[0, 2]

    @zmin.setter
    def zmin(self, v): self[0, 2] = v

    @property
    def zmax(self): return self[1, 2]

    @zmax.setter
    def zmax(self, v): self[1, 2] = v

    @property
    def n_axes(self): return self.origin.shape[0]