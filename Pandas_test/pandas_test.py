import numpy as np
import pandas as pd

obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
sdata = {'Kim': 35000, 'Beomwoo': 67000, 'Joan': 12000, 'Choi': 4000}
obj3 = pd.Series(sdata)
print(obj3)

# Data Frame 정의하기
# 이전에 DataFrame에 들어갈 데이터를 정의해주어야 하는데,
# 이는 python의 dictionary 또는 numpy의 array로 정의할 수 있다.

data = {'name': ['hi', 'hello', 'howdy', 'good morning', 'good afternoon'],
        'year ': [2013, 2014, 2015, 2016, 2015],
        'points': [1.5, 1.7, 3.6, 2.4, 2.9]}

df = pd.DataFrame(data)
print(df)

# 행 방향의 index
print(df.index)

# 열 방향의 index
print(df.columns)

# 값 얻기
print(df.values)
