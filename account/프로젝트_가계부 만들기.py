
"""
프로젝트 : 가계부 만들기
"""


""" 1. 모듈 불러오기 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

df = pd.DataFrame()

plt.rc('font', family='New Gulim')

"""
2. 변수 설명

y = 년도
m = 월
d = 일
cash = 구매 금액
category = 카테고리
store = 거래처
memo = 메모

""" 

""" 3. 데이터 프레임 설정 """
ac_book = pd.DataFrame(columns= ['년도', '월','일','구매금액','카테고리','결제수단','거래처','메모'])

"""
4. 변수 설정 

가계부에서 입력 받은 값 데이터 프레임으로 받음 

"""

y = int(input("년도 : "))
m = int(input("월 : "))
d = int(input("일 : "))
cash = int(input("구매금액 : "))
category = input("카테고리 : ")
method_payment = input("결제수단 : ")
store = input("거래처 : ")
memo = input("메모 : ")

df = pd.DataFrame({'년도' : [y], '월' : [m], '일' : [d], '구매금액' : [cash],
                             '카테고리' : [category],'결제수단' : [method_payment] ,'거래처' : [store], '메모' : [memo]})

ac_book = ac_book.append(df, ignore_index = True)
ac_book.tail()

# --- 만들어진 데이터로 돌리기 ---

account_book = pd.read_excel('C:/Users/juyeo/Desktop/프로젝트_가계부/project_account_book.xlsx')

#결측값 확인, '0'으로 채우기
account_book.isnull().sum()
account_book = account_book.fillna('0')
account_book.isnull().sum()

#날짜 처리 
account_book['년도'] = account_book['년도'].astype(str)
account_book['월'] = '0'+ account_book['월'].astype(str)
account_book['월'] = account_book['월'].str[-2:]

account_book['일'] = '0' + account_book['일'].astype(str)
account_book['일']  = account_book['일'].str[-2:]

account_book['년월'] = account_book['년도'] + '-' +account_book['월']
account_book['년월일'] = account_book['년도'] + account_book['월'] + account_book['일']
account_book['년월일'] = pd.to_datetime(account_book['년월일'])

account_book['주'] = 0


#일주일로 나누기
wk = pd.date_range(account_book['년월일'][0],account_book['년월일'][len(account_book)-1], freq = 'W' )

b = ac_expenditure.groupby(['년월일']).sum()

for i in range(len(wk)-1, -1, -1):
    for j in range(len(account_book['년월일'])-1, -1, -1):
        if account_book['년월일'][j] <= wk[i]:
            account_book['주'][j] = wk[i]


"""-----------------------------"""

#달별 수입, 지출보기
ac_income = account_book['유형'] == '수입'
ac_income = account_book[ac_income]
ac_in = ac_income.groupby(['년월']).sum()

ac_expenditure = account_book['유형'] == '지출'
ac_expenditure = account_book[ac_expenditure]
ac_ex = ac_expenditure.groupby(['년월']).sum()

"""-----------------이번 달 주별 지출 플롯 -------------------"""

def month_week (n):
    n = ('0'+ str(n))[-2 :]
    ac_n = ac_expenditure['월'] == str(n)
    ac_n = ac_expenditure[ac_n]
    ac_n['주'] = ac_n['주'].astype(str)
    ac_n['주'] = ac_n['주'].str[0:10]
    ac_nc = ac_n.groupby(['주'], as_index = True).sum()
    
    plt.plot(ac_nc)
    plt.title((n,'월 주별 지출'))
    return plt.show(), ac_nc




"""--------------------카테고리별 지출 비율 (월 기준)-------------------------"""

#카테고리 함수
def month_category (n):
    n = ('0'+ str(n))[-2 :]
    ac_n = ac_expenditure['월'] == str(n)
    ac_n = ac_expenditure[ac_n]
    ac_nc = ac_n.groupby(['카테고리'], as_index = False).sum()
    ac_nc = ac_nc.sort_values(by = '금액', axis = 0, ascending = False, kind = 'quicksort')
    
    ratio = ac_nc['금액']/ac_nc['금액'].sum()*100
    labels = ac_nc['카테고리']
    colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
    wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
    
    plt.pie(ratio, labels=labels, autopct='%0.f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
    plt.title((n,'월 카테고리별 지출 비율'))
    
    return plt.show()




#8
ac_e8 = ac_expenditure['월'] == '08'
ac_e8 = ac_expenditure[ac_e8]
ac_e8c = ac_e8.groupby(['카테고리'], as_index = False).sum()
ac_e8c = ac_e8c.sort_values(by = '금액', axis = 0, ascending = False, kind = 'quicksort')

ratio = ac_e8c['금액']/ac_e8c['금액'].sum()*100
labels = ac_e8c['카테고리']
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio, labels=labels, autopct='%0.f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.title('8월 카테고리별 지출 비율')
plt.show()

#9
ac_e9 = ac_expenditure['월'] == '09'
ac_e9 = ac_expenditure[ac_e9]
ac_e9c = ac_e9.groupby(['카테고리'], as_index = False).sum()
ac_e9c = ac_e9c.sort_values(by = '금액', axis = 0, ascending = False, kind = 'quicksort')

ratio = ac_e9c['금액']/ac_e9c['금액'].sum()*100
labels = ac_e9c['카테고리']
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio, labels=labels, autopct='%0.f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.title('9월 카테고리별 지출 비율')
plt.show()


#10
ac_e10 = ac_expenditure['월'] == '10'
ac_e10 = ac_expenditure[ac_e10]
ac_e10c = ac_e10.groupby(['카테고리'], as_index = False).sum()
ac_e10c = ac_e10c.sort_values(by = '금액', axis = 0, ascending = False, kind = 'quicksort')

ratio = ac_e10c['금액']/ac_e10c['금액'].sum()*100
labels = ac_e10c['카테고리']
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio, labels=labels, autopct='%0.f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.title('10월 카테고리별 지출 비율')
plt.show()


#11
ac_e11 = ac_expenditure['월'] == '11'
ac_e11 = ac_expenditure[ac_e11]
ac_e11c = ac_e11.groupby(['카테고리'], as_index = False).sum()
ac_e11c = ac_e11c.sort_values(by = '금액', axis = 0, ascending = False, kind = 'quicksort')

ratio = ac_e11c['금액']/ac_e11c['금액'].sum()*100
labels = ac_e11c['카테고리']
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio, labels=labels, autopct='%0.f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.title('11월 카테고리별 지출 비율')
plt.show()


#12
ac_e12 = ac_expenditure['월'] == '12'
ac_e12 = ac_expenditure[ac_e12]
ac_e12c = ac_e12.groupby(['카테고리'], as_index = False).sum()
ac_e12c = ac_e12c.sort_values(by = '금액', axis = 0, ascending = False, kind = 'quicksort')

ratio = ac_e12c['금액']/ac_e12c['금액'].sum()*100
labels = ac_e12c['카테고리']
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio, labels=labels, autopct='%0.f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.title('12월 카테고리별 지출 비율')
plt.show()


#01
ac_e01 = ac_expenditure['월'] == '01'
ac_e01 = ac_expenditure[ac_e01]
ac_e01c = ac_e01.groupby(['카테고리'], as_index = False).sum()
ac_e01c = ac_e01c.sort_values(by = '금액', axis = 0, ascending = False, kind = 'quicksort')

per = ac_e01c['금액']/ac_e01c['금액'].sum()*100
#ac_e01c = ac_e01c.assign(비율 = per)

ratio = per
labels = ac_e01c['카테고리']
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio, labels=labels, autopct='%0.f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.title('1월 카테고리별 지출 비율')
plt.show()


"""-----------------6개월간의 지출, 수입 + 지출 분석-------------------"""

fig,axes = plt.subplots(ncols = 1,sharey = True, figsize = (10,5))
fig.suptitle('6개월간 지출, 수입 변화')

sns.lineplot(x = '년월', y = '금액', data = ac_in)
sns.lineplot(x = '년월', y = '금액', data = ac_ex)

ac = ac_in - ac_ex

plt.plot(ac)

