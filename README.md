# splitsort
First experiment in checking ChatGPT Computer Science potential by dealing with the sorting problem. I've asked ChatGPT for a new, not necessarily the best, sorting algorithm and it came up with Splitsort, the algorithm which I've implemented with its help, first in Python, then in C and finally making it usable in Python, but still as a C library compiled. As a last step I've added a loop in Python that tests the library for correctness. I believe the result is above the average for code that sorts a list of integers. 

The concept came from the idea that, while Computer Science students, people are incentivized to do things from scratch by themselves, reinventing the wheel as a result, but, as professional practioners, specially as software engineers, people are pushed to, as often as possible, not write their own code, but use what already exists instead and, in a way, programming with the help of large language models is the culmination of that. The overall conclusion is that code is only worthy if it is for a new thing. That fact might push dealing with all the lower level aspects of digital technology to a select few. So, what if we can have a new thing to implement without being one of those few with the help of the same tool that promises to make programmers not needed? That is what motivated this little project. The same process can be much more interesting with more advanced problems, including in the machine learning field.

Instructions for compiling the library at Windows:

cl.exe /c /MD /Fo"./" /Fe"splitsort.dll" splitsort.c
link /out:splitsort.dll /dll /implib:splitsort.lib splitsort.obj

Make sure you are using the proper Visual Studio Developer command prompt. You might need to use x64 Native Tools Command Prompt
