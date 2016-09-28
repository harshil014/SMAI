from datetime import date

def diff_dates( date1, date2):
	return abs(date2-date1).days

def func():
	x=input()
	print x


def main():
	
    d1 = date(2013,1,1)
    d2 = date(2016,1,1)
    result1 = diff_dates(d2, d1)
    print '{}'.format(result1)
    
func()

main()