#import mymodule

#mymodule.say_hi()

#print ('Version', mymodule.__version__)

from mymodule import say_hi, __version__

say_hi()

print ('Version', __version__)

import sys

print("## sys.dir :", dir())

print(" __annotations__ : {}".format(__annotations__))
print(" __builtins__ : {}".format(__builtins__))
print(" __cached__ : {}".format(__cached__))
print(" __doc__ : {}".format(__doc__))
print(" _file__ : {}".format(__file__))
print(" __loader__ : {}".format(__loader__))
print(" __name__ : {}".format(__name__))
print(" __package__ : {}".format(__package__))
print(" __spec__ : {}".format(__spec__))
print(" __version__ : {}".format(__version__))
print(" sys : " + str(sys))
