def con(a,b,i,c):
   global o_dif
   if c == 2:
       con(a,b,i, 1)
       con(a,b,i, 0)
   if i == len(list)-1:
       if c == 1:
           a += list[i]
           b -= list[i]
       dif = b-a
       if abs(dif)<abs(o_dif):
          o_dif = dif
   else:
       if c == 1:
           a += list[i]
           b -= list[i]
       con(a,b,i+1,1)
       con(a,b,i+1,0)

s = input()
s_list = s.split(' ')
list = [int(i) for i in s_list]
a = 0
b = sum(list)
i = 0
o_dif = sum(list)
con(a,b,i,2)
print(abs(o_dif))
