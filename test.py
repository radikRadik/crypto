
import random



def add_space(s):
	a = '9gf4nlbk7pcith5mra1s3edvz802qou6xwjy'
	lst = list(a)
	lst2 = list(a)

	random.shuffle(lst)
	aggiunta = "".join(lst)

	random.shuffle(lst2)
	aggiunta_finale = "".join(lst2)

	index_start = random.randint(1,35)
	index_end = random.randint(1,35)
	s = (a[index_start] + a[index_end] + aggiunta[index_start:]+ s + aggiunta_finale[:index_end] )
	return s


def remove_space(s):
	a = '9gf4nlbk7pcith5mra1s3edvz802qou6xwjy'
	lst = list(a)

	n = a.index(s[0])
	n_finale = a.index(s[1])
	aggiunta = len(lst[n:])

	ns = s[aggiunta+2:]

	return ns[:-n_finale]



# sd2r3l7wojqnitb0hxec

a = add_space("a")

print(a)

print(remove_space(a))