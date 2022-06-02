# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pandas._config import get_option
from pandas._libs import lib
from pandas.compat._optional import import_optional_dependency
from pandas.util._decorators import Appender
from pandas.core.dtypes.common import is_float
import pandas as pd
from pandas.api.types import is_dict_like, is_list_like
import pandas.core.common as com
from pandas.core.generic import _shared_docs
#from pandas.core.indexing import _maybe_numeric_slice, _non_reducing_slice
import_optional_dependency("jinja2", extra="DataFrame.style requiresjinja2.")


import streamlit as st
#import Jinja2
st.write("hello")
