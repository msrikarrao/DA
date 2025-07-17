from copy import *
names = ["M Srikar Rao", "G Pradeep", "G Sandeep"]
newNames = deepcopy(names)
print(F"Original names list : {names}")
print(F"Deep copied names list : {newNames}")
names.append("Shasthri")
print(names)
print(newNames)