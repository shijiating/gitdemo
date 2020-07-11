from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

customer_data = pd.read_csv(r'svmdata.csv',encoding = 'GB2312')
df = pd.DataFrame(customer_data,columns=['whole_illegaltimes','twoyear_illegaltimes'
                          ,'is_halfyear_illegal','maximum_cigar_num','outofprovince_times','maximum_outofprovince_num'
                          ,'is_criminal','business_format','is_sensitivecircle','is_downgrade'
                          ,'is_sensitive_canton','is_sensitive_nativeplace','purchase_change','sell_change'
                          ,'sales_ratio','sensitive_time'])
print(df)
df.business_format[df.business_format =='TOP'] = 1
df.business_format[df.business_format =='MIDDLE'] = 2
df.business_format[df.business_format =='LOW'] = 3

df.sensitive_time[df.sensitive_time =='TOP'] = 1
df.sensitive_time[df.sensitive_time =='MIDDLE'] = 2
df.sensitive_time[df.sensitive_time =='LOW'] = 3
print(type(df))



# 独热编码处理
# from sklearn.preprocessing import OneHotEncoder
# X=customer_data.iloc[:,10:11]
# Y=customer_data.iloc[:,18:19]
# print(type(X))
# print(Y)
# enc=OneHotEncoder(categories='auto').fit(X)
# result=enc.transform(X).toarray()
# pd.DataFrame(enc.inverse_transform(result))
# f1=enc.get_feature_names()
#
# enc=OneHotEncoder(categories='auto').fit(Y)
# result2=enc.transform(Y).toarray()
# pd.DataFrame(enc.inverse_transform(result2))
# f2=enc.get_feature_names()
# print(f1)
# print(f2)
#
#
#
# customer_data=customer_data.reset_index(drop=True)
# newcustomer_data=pd.concat([customer_data,pd.DataFrame(result)],axis=1)
# newcustomer_data.drop(["business_format"],axis=1,inplace=True)
# newcustomer_data=pd.concat([customer_data,pd.DataFrame(result2)],axis=1)
# newcustomer_data.drop(["sensitive_time"],axis=1,inplace=True)
# newcustomer_data.columns=['created_at','is_delete','store_id','whole_illegaltimes','twoyear_illegaltimes'
#                           ,'is_halfyear_illegal','maximum_cigar_num','maximum_outofprovince_num','outofprovince_times'
#                           ,'maximum_outofprovince_num','is_criminal','is_sensitivecircle','is_downgrade'
#                           ,'is_sensitive_canton','is_sensitive_nativeplace','purchase_change','sell_change'
#                           ,'sales_ratio','bussinessformat_LOW','bussinessformat_MIDDLE'
#                           ,'bussinessformat_TOP','sensitivetime_LOW'
#                           ,'sensitivetime_MIDDLE','sensivetime_TOP']

# print(newcustomer_data)

# df=df.reset_index(drop=True)
# newcustomer_data=pd.concat([customer_data,pd.DataFrame(result)],axis=1)

# newcustomer_data=df.drop(columns=["created_at", "is_delete"], axis=1, inplace=False)
# print(type(newcustomer_data))
print(df)
scaler=StandardScaler()
# # scaler.fit(newcustomer_data)
x_std=scaler.fit_transform(df)
print(x_std)

# newcustomer_data.describe([0.01,0.05,0.1,0.25,0.5,0.75,0.9,0.99]).T