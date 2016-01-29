all:
	rm -f *.so *.o *_wrap.* *.pyc
	swig -python example.i
	gcc -c -fPIC example.c -example.o
	gcc -c -fPIC example_wrap.c -I/usr/include/python2.7
	gcc -shared  example.o example_wrap.o -o _example.so

clean:
	rm -f *.so *.o *_wrap.* *.pyc
