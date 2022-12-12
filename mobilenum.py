
import re 

def main():
	fd=open ("phonenum.txt",'r')
	num=fd.readline()

	for num in fd:
	    print(num)
	    r=re.fullmatch('[6-9][0-9]{9}',num)
	    print(r)
	    if r!=None: 
		print('Valid Number')
	    else:
		print('Not a valid number')

if __name__ == "__main__":
main()
