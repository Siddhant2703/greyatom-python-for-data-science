# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data,new_record))
print(data.shape)
print(census.shape)

#Step2

age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

#step3

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
minority_race=min(len_0,len_1,len_2,len_3,len_4)
print(minority_race//2)

#Step4

senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len= len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(working_hours_sum)
print(avg_working_hours)

#Step5

high=census[census[:,1]>10]
low=census[census[:,1]<=10]
pay_high=high[:,7]
pay_low=low[:,7]
avg_pay_high=pay_high.mean()
avg_pay_low=pay_low.mean()
print(avg_pay_high)
print(avg_pay_low)


