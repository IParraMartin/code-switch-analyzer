![GitHub repo file count](https://img.shields.io/github/directory-file-count/IParraMartin/code-switch-analyzer)
![GitHub repo size](https://img.shields.io/github/repo-size/IParraMartin/code-switch-analyzer?color=red)

# Code-switch-analyzer
A python code to analyze code-switching data.

The script includes a function that reads textual data and outputs languge use percetage and plots. 
A downloadable .csv file is also available –if desired.

Even if the code is easy to use, it requires some coding knowledge. 
The user must be able to create strings (e.g 'this is a string') and call functions (e.g this_function(calls_this_input)).
The whole project is based on a singel function that creates everything else.

On dictionaries
---------------
Files 'en' and 'sp' are the dictionaries that the code uses to check if the word is in English or in Spanish. The code 'redirects' the query to the dictionaries and checks if the given token is in one or the other. Thus, it is necessary to have adequate dictionary sizes to enhance the performance of the code.

Who is this for?
---------------
- Researchers on linguistics and NLP focused on code-switching tasks
- General linguistics researchers

Benefits
---------------
- Easy to use and implement
- Pipelines the phrase analysis by automatizing monotonic processes such as data classification and plot making

Limitations
----------------
- Code not ready for general purposes:
  1. Needs more dictionary
  2. Needs to improvements to analyze full datasets
- Only ready for Spanish and English code-switches
