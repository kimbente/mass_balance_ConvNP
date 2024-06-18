
import xarray as xr
import numpy as np
import pandas as pd

def construct_circ_and_linear_time_ds(dates, freq):
    """
    Return an :class:`xarray.Dataset` containing a circular variable for time.
    The ``freq`` entry dictates the frequency of cycling of the circular
    variable. E.g.:
    Note: Can be applied after preprocessing since outputs are normalised.

        - ``'H'``: cycles once per day at hourly intervals
        - ``'D'``: cycles once per year at daily intervals
        - ``'M'``: cycles once per year at monthly intervals

    Args:
        dates (...):
            ...
        freq (...):
            ...

    Returns:
        :class:`xarray.Dataset`
            ...
    """
    # Ensure dates are pandas
    dates = pd.DatetimeIndex(dates)
    if freq == "D":
        time_var = dates.dayofyear
        mod = 365.25
    elif freq == "H":
        time_var = dates.hour
        mod = 24
    elif freq == "M":
        time_var = dates.month
        mod = 12
    else:
        raise ValueError("Circular time variable not implemented for this frequency.")

    cos_time = np.cos(2 * np.pi * time_var / mod)
    sin_time = np.sin(2 * np.pi * time_var / mod)
    # normalised year
    year_time = (((dates.year - dates.year.min())/(dates.year.max() - dates.year.min()) * 2) - 1)

    ds = xr.Dataset(
        coords = {"time": dates},
        data_vars = {
            f"cos_{freq}": ("time", cos_time),
            f"sin_{freq}": ("time", sin_time),
            f"year": ("time", year_time),
        },
    )
    return ds