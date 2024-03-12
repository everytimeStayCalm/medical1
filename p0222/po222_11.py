print( '-' *35)
print('\t[학생성적입력]')
print( '-'*35)
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적삭제')
print('4.학생성적전체출력')
print('5.학생검색출력')
print('6.등수처리')
print('')

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(1, '홍길동',100,100,100,300,100.0,1))
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(1, '유관순',90,100,90,(90+100+900),(90+100+90)/3,1))
#stu_no1, stu_n02, stu_name1, stu_name2, kor1, kor2
#eng1, eng2, math1, math2, total1, total2, avg1, avg2
stu_name1= input('첫번째 학생이름을 입력하세요>>')
stu_name2= input('두번째 학생이름을 입력하세요>>')
print('홍길동님 합격입니다')
print('홍길동님 불합격입니다')

