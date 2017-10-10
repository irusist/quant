import os
from datetime import date


today = date.today().strftime('%Y%m%d')
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "xueqiu", "ccs", today))