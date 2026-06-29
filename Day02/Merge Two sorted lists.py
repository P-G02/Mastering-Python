'''Merge Two sorted lists'''

my_list1=[4,5,9,3,0,20]
my_list2=[1,6,10,25,30,35]

my_list1.sort()
my_list2.sort()

my_list1.extend(my_list2)

my_list1.sort()
print(my_list1)