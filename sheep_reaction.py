
  import math
  import xlrd
  import xlsxwriter
  import pandas as pd
  import numpy as np
  import mixed
  
  
  gr = np.array(pd.read_excel('MI_sheep.xlsx',header=None))
  gr = np.delete(gr,(0),axis = 1);
  gr = np.delete(gr,(0),axis = 0);
