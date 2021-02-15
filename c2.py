class Sampleclass:
	count = 0
	def increase(self):
		Sampleclass.count+=1
a=Sampleclass()
a.increase()
print(a.count)		
b=Sampleclass()
b.increase()
print(b.count)
print(Sampleclass.count)