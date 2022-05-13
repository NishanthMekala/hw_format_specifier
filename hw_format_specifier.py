'''Using %s(string insert)'''
print('I am a %s boy.'%('good'))#I am a good boy.
print('%s was created by %s.'%('Python', 'Guido Van Rossum'))#Python was created by Guido Van Rossum.

'''Using %d(intergar insert)'''
print('He is %dyrs old.'%(66))#He is 66yrs old.
print('He was born on %dst %s %d.'%(31, 'Jan', 1956))#He was born on 31st Jan 1956.

'''Using %f(float insert)'''
print('The value of π is %1.15f' %3.141592653589793)#The value of π is 3.141593.
print('The dimensions of the cuboid is %1.1f×%1.0f×%1.2f'%(10.5, 5,6.25))#

'''Using format() '''
print('Python was created in {}.'.format('Centrum Wiskunde & Informatica(CWI)'))
print('I {0} {1}'.format('love','programming'))

'''Using Fast strings'''
a='Python3'
print(f'I am learning {a}')
b= 15
c= 15
print(f'15 spuare is {b*c}')