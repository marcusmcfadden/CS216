import pandas as pd
mystery1 = pd.Series({'zero':0, 'one':1, 'two':2, 'three':3})
mystery2 = pd.Series({'one':1, 'two':2, 'three':3, 'four':4})
print(mystery1 + mystery2)