# Take input with EOF in Python
You already have your test case files and their expected outputs. If you have followed the missing semester course I mentioned during first week, you probably know this tip already. 

In a terminal you can run your hw code like this. 

```bash
$ python hw1.py < test.in > test.out 
```


# Testing Tips

More specifically, you can check your output using the -Z option of the diff. If you get no diff like below, it means you have passed the test case.

```bash
$ diff -Z  test1.myoutput test1.expected 
$
```


