def sus(parameters):
 if parameters:
  print(parameters)
  chisla=parameters
  index_out=[]
  dovj=len(chisla)
  for i in range(dovj):
   if not(i in index_out):
    index_out.append(i)
    for k in range(i+1,dovj):
     if not(k in index_out):
      if int(chisla[i])+int(chisla[k])==10:
       index_out.append(k)
       print(chisla[i],"+",chisla[k],"=10")
       break
if __name__ == '__main__':
 import sys
 sus(sys.argv[1:])
