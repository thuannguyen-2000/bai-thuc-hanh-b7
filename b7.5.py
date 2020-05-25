def file_read(fname):
    from itertools import islice
    with open(fname, "w") as myfile:
        myfile.write("python Exercies\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())
file_read('abc.txt')
        
