import sys

input = sys.stdin.readline

amount = int(input())

r_price = 1000 - amount 

m_500 = r_price //500 
r_price = r_price % 500

m_100 = r_price //100
r_price = r_price % 100 

m_50 = r_price // 50 
r_price = r_price % 50 

m_10 = r_price // 10 
r_price = r_price % 10 

m_5 = r_price // 5 
r_price = r_price % 5

m_1 = r_price // 1 

print(m_500 + m_100 + m_50 + m_10 + m_5 + m_1)



