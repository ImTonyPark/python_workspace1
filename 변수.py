'''
변수
-무언가(데이터)를 저장하기 위한 공간
-변수 이름 작성 규직
-의미 부여하여 만든다
-이름은 영어로 만든다
-또한 영어+숫자도 가능
-보통 3~10자 이내로 만든다
-키워드는 사용하면 안된다
'''

#import keyword
#print (keyword.kwlist) #잘 사용하지는 않는다~

num = 100
print(num+200) # 변수 부여하면더하기해도됨
print(num*2000, "살 입니다")

n = 5
print('변경 전 n:',n)
n = n+10
print(f'변경후 n : {n}')  

n1 = 5; n2 = 10;
sum_ = n1 + n2
print( f'{n1} + {n2} = {sum_}')
#print = 100 # 이렇게 적으면 작동 안한다. 참고

num1 = 10; num2 = 20; 
num3 = num1 + num2
print( f'num1({num1}) + num2({num2}) = {num3}')
#이렇게도 된다.
print("num1(",num1,") + num2(",num2,")= ", num3)
print("num1({})+num2({})={}".format(num1,num2,num3))  #format 활용하면 이렇게도 된다;;;

flt = 123.456
print("flt :", flt)
print("rount(flt) :", round(flt))  #반올림 안되는값 짤라버려서 123. 나머지 짤림
print("rount(flt,1) :", round(flt,1)) #소수점1번쨰꺼
print("rount(flt,2) :", round(flt,2)) #소수점2번쨰꺼


py = 40
c = 60
java = 90
total = py+c+java
print("3과목 점수 합계", total)
print("3과목 점수 평균", round(total/3,2))


sa = 11
sa1 = 37
print("한역을 지나는데 걸리는 시간은 총",round(sa1/sa,2),"입니다") 


weight = 260
f = 14
f1 = 500.23
ft = f1 + (f-1)*weight 
print("이건물의 높이는",round(ft,3),"m입니다")

