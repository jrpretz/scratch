all: hello control types class memory references parallel mymodule_main

parallel: parallel.d
	dmd parallel.d -of=parallel

references: references.d
	dmd references.d -of=references

memory: memory.d
	dmd memory.d -of=memory

class: class.d
	dmd class.d -of=class

hello: hello.d
	dmd hello.d -of=hello

control: control.d
	dmd control.d -of=control

types: types.d
	dmd types.d -of=types

mymodule_main: mymodule_main.d mymodule.d
	dmd mymodule_main.d mymodule.d -of=mymodule_main

clean:
	rm -f hello hello.o
	rm -f control control.o
	rm -f types types.o
	rm -f class class.o
	rm -f memory memory.o
	rm -f references references.o
	rm -f parallel parallel.o
	rm -f mymodule_main mymodule_main.o
