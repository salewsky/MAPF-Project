def instance_rep(instance):
	instance = instance.replace("%","")
	return instance
	
def testing(instance):
	print(instance)
	instance = instance_rep(instance)
	print(instance)


instance= "%Das ist ein Test"
testing(instance)
