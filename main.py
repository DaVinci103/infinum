from functools import cache

class Num:
	def __init__(self, arg):
		match arg:
			case int() | float():
				self.val = {0: arg}

			case dict():
				self.val = {int(i): float(arg[i]) for i in filter(lambda i: arg[i] != 0, arg)}

			case Num():
				self.val = {i: arg.val[i] for i in arg.val}

			case _:
				raise Exception(f"{type(arg)} type not supported in Num.__init__()")

	@cache
	def __abs__(self):
		if not self:
			return self

		it = iter(self)
		m = next(it)
		return self if m > 0 else -self

	def __add__(self, other):
		if type(other) != Num:
			other = Num(other)

		return Num({i: self[i] + other[i] for i in {*self.val, *other.val}})

	def __and__(self, other):
		return Num({i: self[i] & other[i] for i in {*self.val, *other.val}})

	def __bool__(self):
		return self.val != {}

	@cache
	def __ceil__(self):
		return Num({0: self[0], **{i: ceil(self.val[i]) for i in filter(lambda x: x > 0, self.val)}})

	def __eq__(self, other):
		return type(other) == Num and self.val == other.val

	@cache
	def __float__(self):
		it = iter(self)
		m = next(it)
		if m > 0:
			raise Exception(f"cannot convert an infinite number ({self}) to a float")

		return self[0]

	def __format__(self):
		return str(self)

	def __getitem__(self, i):
		if i in self:
			return self.val[i]

		return 0

	def __iter__(self):
		l = [i for i in self.val]
		l.sort(reverse = True)
		return iter(l)

	@cache
	def __neg__(self):
		return Num({i: -self.val[i] for i in self.val})

	def __radd__(self, other):
		return self + other

	def __rsub__(self, other):
		return (-self) + other

	@cache
	def __str__(self):
		return " + ".join(f"{self.val[i]}ω^{i}" for i in self)

	def __sub__(self, other):
		return self + (-other)







