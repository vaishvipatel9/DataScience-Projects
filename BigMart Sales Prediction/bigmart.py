from pyforest import*
lazy_imports()

import warnings
warnings.filterwarnings("ignore")

Train_data=pd.read_csv("train.csv")
Test_data=pd.read_csv("test.csv")

Train_data.head()
Test_data.head()

print('Train_data:',Train_data.shape)
print('Test_data:',Test_data.shape)

Train_data.describe().T

print (Train_data.isnull().sum())
print (Test_data.isnull().sum())
