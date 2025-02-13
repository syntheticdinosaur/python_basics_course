# Python Basics  

Welcome to **Python Basics**, a structured introduction to Python programming. This course covers fundamental concepts, data structures, functions, and essential libraries like NumPy and Matplotlib. Through hands-on exercises, you'll build a solid foundation for practical programming.  

__About this Course__   

This course was developed at the Institute for Neuromodulation and Neurotechnology at the University and University Hospital Tuebingen, Germany. We have used similar notebooks to teach undegraduates for data analysis in our course "Neuromodulation and Neuroplasticity". We have adapted the materials to be for a more general audience, but applications and exercise of course still show its neuroscientific origins.

__Course Authors__   
Joshua P. Woller, M.Sc.     (@syntheticdinosaur)   
David Menrath, M.Sc.        (@DavidMenrath)

## Getting Started

To use Jupyter Notebooks, you typically need **Python** installed on your computer. However, to make it easier to get started without any setup, you can run the notebooks directly in your web browser using online services. This allows you to start coding right away without installing anything.

Below, we present different ways to run the notebooks. Choose the option that best fits your needs.

[Here](jupyter_nb_intro.md) you can find more information on Jupyter Notebooks.

### Running the Notebooks

#### 1. Run Online with Binder

Binder lets you run Jupyter Notebooks directly in your web browser without installing anything. This is the easiest way to get started quickly. However, Binder does not save your changes permanently, so if you modify the notebooks, you need to **download your work manually** before closing the session.

**Click below to launch the course in Binder:**

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/syntheticdinosaur/python_basics_course/main)

#### 2. Run Online with Google Colab

Google Colab is a free cloud-based notebook service provided by Google. It allows you to run Jupyter Notebooks without any installation. One key advantage is that Colab **automatically saves your work in Google Drive**, making it easy to continue where you left off. However, you will need a **Google account** to use it, and some advanced Python libraries may require additional setup.

**Click below to open the course in Google Colab:**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DavidMenrath/notebook_testing/blob/main)


#### 3. Run Online with GitHub Codespaces

GitHub Codespaces allows you to run the notebooks in a full **VS Code environment in your browser**. This option provides a more powerful development environment and **automatically saves your work**, but it requires a GitHub account and may have resource limitations on free accounts.

**Click below to launch the course in GitHub Codespaces:**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?repository_id=931132863)


#### 4. Run Offline on Your Computer

If you already have Python installed on your computer, you can **download** the notebooks and run them locally. This allows you to work in your own environment with full control over your files and installed libraries. You can either **download** the repository as a ZIP file and extract it. If you are familiar with GitHub, you can also **clone** the repository using Git to keep it organized on your machine. If you prefer to keep your own version and track changes, you can **fork** the repository on GitHub and work with it independently. Running the notebooks locally requires Python and Jupyter Notebook to be set up on your system.



## Table of Contents  
0. **Core Python** – Variables, data types, lists, and control flow  

    01. [Introduction to Python Programming](0_Introduction/01_Intro_First_Steps.ipynb)  
    Overview of programming, variables, and the first steps in Python using a "Hello World" program.

    02. [Python as a Calculator](0_Introduction/02_Basics_Calculator.ipynb)  
    Perform basic math operations, and equality testing.

    03. [Using Variables](0_Introduction/03_Basics_Variables.ipynb)  
    Learn how to create, assign, and update variables in Python.

    04. [Variable Types](0_Introduction/04_Basics_DataTypes.ipynb)  
    Introduction to different variable types in Python (e.g., int, str, float, bool) and how to determine and work with them.

    05. [List Basics](0_Introduction/05_Lists_Basics.ipynb)  
    Introduction to creating and manipulating lists in Python, including indexing and slicing.

    06. [Further List Operations](0_Introduction/06_Lists_Operations.ipynb)  
    Learn about merging and combining lists, removing and replacing elements from lists.

    07. [Sets and Dictionaries](0_Introduction/07_Sets_Dictionaries.ipynb)  
    Introduction to other iterables such as sets and dictionaries, and their differences to lists.

    08. [Logical Operations](0_Introduction/08_Logical_Operations.ipynb)  
    Introduces boolean or logical values, as well as logical operators such as 'and', 'or', 'xor', and 'not'.

    09. [Control Flow](0_Introduction/09_ControlFlow_Loops.ipynb)  
    Shows conditional code execution in if-elif-else statements, and for-loops as well as while-loops.

1. **Functions & Advanced Concepts** – Functions, classes, and modules  


    01. [Functions: Basics](1_Functions_Classes_Modules/10_Functions_Basics.ipynb)  
        How to create and call basic functions, and how to use return statements in functions.  

    02. [Functions: Advanced](1_Functions_Classes_Modules/11_Functions_Advanced.ipynb)  
        Using default arguments in functions, cautionary notes on variable scope and an introduction to documenting your code using docstrings.  

    03. [Mutability](1_Functions_Classes_Modules/12_Advanced_Mutability.ipynb)  
        We discuss mutable and immutable datatypes, how to test for the identity of objects, and consequences of passing mutable objects between caller and function.  

    04. [Classes and Objects](1_Functions_Classes_Modules/13_Advanced_ClassesObjects.ipynb)  
        Introduces the concept of classes, and how to create objects. Also provides a glimpse at .set() and .get() methods to safely extract or modify class attributes.  

    05. [Modules](1_Functions_Classes_Modules/4_Advanced_Modules.ipynb)  
        Teaches how to import (and install) external modules, how to use their functions, and how to use aliases for modules.  

    06. [Dataclasses: Basics](1_Functions_Classes_Modules/15_Advanced_Dataclasses.ipynb)  
        Shows the concept of dataclasses, which are a compact way to represent linked data using specific objects.  

    07. [Dataclasses: Fields](1_Functions_Classes_Modules/16_Advanced_DataclassFields.ipynb)  
        Introduces the concept of fields, which prevents multiple instances of a class from sharing ownership of the same mutable object if such behavior is not desired.  

2. **NumPy** – Efficient numerical computing  

    01. [Introduction to NumPy](2_Numpy/20_NumPy_Intro.ipynb)  
        In this notebook, we show how to import NumPy and how to create a basic NumPy array from an existing Python list.   

    02. [NumPy Array Types](2_Numpy/21_NumPy_ArrayTypes.ipynb)  
        Introduces various datatypes an array can hold, and the concept that a NumPy array casts all contained elements to a single shared type.  

    03. [Array Shapes](2_Numpy/22_NumPy_ArrayShapes.ipynb)  
        Discusses shapes, and their influence on combining arrays, e.g. by arithmetic operations. We also discuss how to change the shape of arrays to make them compatible.   

    04. [Mutability](2_Numpy/23_NumPy_Mutability.ipynb)  
        We discuss the concept of views vs copies in NumPy, how that relates to the concept of mutability we learned before, and the practical implications thereof.  

    05. [Numerical Operations](2_Numpy/24_NumPy_NumericalOps.ipynb)  
        An overview of numerical operations between different arrays, or summary operations such as taking the mean, on individual arrays. Showcase for a lot of the potential operations supported by NumPy.  

    06. [Array Manipulations](2_Numpy/25_NumPy_Manipulations.ipynb)  
        How to combine and extend arrays.  

    07. [Efficiency](2_Numpy/26_NumPy_Efficiency.ipynb)  
        A short introduction showing computational advantages of NumPy arrays.  

3. **Matplotlib** – Data visualization basics  
    01. [Introduction to Matplotlib](3_Matplot/30_Matplotlib_Intro.ipynb)  
        This notebook provides an introduction to matplot, shows how to create and adapt simple plots, and showcases the different types of plots the library has to offer.  
    
    02. [Styling and Export](3_Matplot/31_Matplotlib_StylingExport.ipynb)  
        In this notebook, we discuss ways to individualize plots and to prepare them for export in various file formats.  
        
