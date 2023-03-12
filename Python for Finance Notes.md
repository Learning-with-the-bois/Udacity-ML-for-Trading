
# Python For Finance by Yves Hilpisch

## Chapter 1

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. It is characterized by the 
following features: open source, interpreted, multiparadigm – supports different programming and implementation paradigms-, multipurpose, 
cross-platform, dynamically typed, indentation aware, and garbage collecting.

A major feature of Python as an ecosystem is the availability of a large number of libraries and tools.

Python does not only appeal to professional software developers; it is also of use for the casual developer as well as for domain experts 
and scientific developers. 

The scientific stack is: NumPy, SciPy, matplotlib, PyTables, and pandas.


Technology has become a major asset for almost any financial institution around the globe, having the potential to lead to competitive 
advantages as well as disadvantages.

Banks and financial institutions together form the industry that spends the most on technology on an annual basis.

The technological development has also contributed to innovations and efficiency improvements in the financial sector, but there 
are naturally other inherent increased risks and risk management, oversight and regulation becomes much more complex.

On the one hand, technology advances reduce cost over time, ceteris paribus. On the other hand, financial institutions continue to 
invest heavily in technology to both gain market share and defend their current positions.

On the one hand, increasing data availability on ever-smaller scales makes it necessary to react in real time. On the other hand, 
the increasing speed and frequency of trading let themdata volumes further increase. This leads to processes that reinforce each 
other and push the average time scale for financial transactions systematically down. 

Some challenges that the greatly increased data flow present are data processing -understanding what is happening at any given time-, 
analytics speed, and theoretical foundations -having robust concepts and theories of the economy.

There is one discipline that has seen a strong increase in importance in the finance industry: financial and data analytics. 
It refers to the discipline of applying software and technology in combination with (possibly advanced) algorithms and methods 
to gather, process, and analyze data in order to gain insights, to make decisions, or to fulfill regulatory requirements, for instance. 

Some of the aspects worth highlighting of Python for finance are its simple syntax, its ease of math to code translation and the power of vectorization. 

We have:

* English for writing, talking about scientific and financial problems, etc.

* Mathematics for concisely and exactly describing and modeling abstract aspects, algorithms, complex quantities, etc.

* Python for technically modeling and implementing abstract aspects, algorithms, complex quantities, etc. 


At a high level, benefits from using Python can be measured in three dimensions:

* Efficiency: saving time

* Productivity: improve resource use

* Quality: unique capacitites

Aside note: Can use pandas.io.data as web to read data, i.e. web.DataReader(name, data_source, start, end dates)

Python is often seen as very slow as it’s an interpreted language, but it doesn’t have to be. Three strategies to improve performance are:

* Paradigm: Choosing the right way (libraries, methods, code optimization, etc.).

* Compiling: using compiled versions of functions. (ie Cython and Numba)

* Parallelization

Python per se is not a high-performance computing technology. However, Python has developed into an ideal platform to access current 
performance technologies. In that sense, Python has become something like a glue language for performance computing.

Example of optimizing a code in page 27 (pdf)  some cool tricks were using the methods of numexpr, ne:  .set_num_threads(n) for
parallelism, and ne.evaluate(‘function’) for the calculation itself.

Another important benefit of Python is that it can be used end to end, from prototyping to production.

<sub>Date: March 11&12, 2023. Time spent: 2.5 hours. Total: 2.5 hours</sub>