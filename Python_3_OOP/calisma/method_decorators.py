from abc import ABC, abstractmethod


class MyClass():

	def __init__(self, name="MyClass"):
		self.name = name

	def instance_method(self):
		print(f"This is an instance method of {self.name}.")
	
	@classmethod
	def class_method(cls):
		print(f"This is a class method of {cls.__name__}.")
	
	@staticmethod
	def static_method():
		print(f"This is a static method of {MyClass.__name__}.")

	# @abstractmethod
	# def abstract_method(self):
	# 	print(f"This is an abstract method of {self.name}.")

	@property
	def my_property(self):
		print(f"This is a property of {self.name},  and used to write a getter for name attribute .")
		return self.name
	@my_property.setter
	def my_property(self, value):
		print(f"This is a property of {self.name},  and used to write a setter for name attribute .")
		self.name = value


MyClass.static_method() 
MyClass.class_method()
#MyClass.instance_method()  #hata: instance bekler
#MyClass.abstract_method()  #hata: instance bekler, ayrıca abstract method olduğu için hata verir

obj = MyClass("obj")
obj.instance_method()
obj.class_method()  # instance üzerinden de çağrılabilir
obj2 = MyClass("obj2")
#obj2.abstract_method()  # This is an abstract method. 