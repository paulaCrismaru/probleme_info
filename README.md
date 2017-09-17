Problemele sunt scrisein Python, nu in C++, deci nu te apuca sa dai copy-paste.
Nu baga in seama lucrurile ce tin de limbaj (def, with('....',' r') open as, xrange etc)

Echivalente:

- 
    - for i in xrange(1, 5)
    - for(i=1; i<5; i++){
      ...
    }
- 
    - print("Hello world")
    - cout<<"Hello world";
- 
    - with('file.in', 'r') as f:
        ...
    - ifstream fin('file.in');
        ...
  