import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dta = [1,2,4,8,16]
dta = pd.Series(dta)
diff1 = dta.diff(1)
diff2 = diff1.diff(1)
diff3 = dta.diff(2)
print(dta)
print(diff2)
print(diff3)

