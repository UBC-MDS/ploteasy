
# ploteasy

![](https://github.com/fei-chang/ploteasy/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/fei-chang/ploteasy/branch/main/graph/badge.svg)](https://codecov.io/gh/fei-chang/ploteasy) ![Release](https://github.com/fei-chang/ploteasy/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/ploteasy/badge/?version=latest)](https://ploteasy.readthedocs.io/en/latest/?badge=latest)

This is a python package that offers beginner-friendly functions to do data visualizations. The functions have build-in theme and other settings, which are complicated for the beginners of python but are compulsory for plotting in mainstream plotting packages like Altair. Also, potential users of Altair may take baby steps from PlotEasy, for its intuitive way to use and its similarity with the most well-know panda functions. PlotEasy can minimize the code when calling a plot in Python, and can path your journey to EDA as smooth as silk!


The main components of this package are:

- **Drawing histogram plot**
  A histogram is an approximate representation of the distribution of numerical data, and an effective indication of the distribution of non-discrete variables.To construct a histogram using Ploteasy, people do not have to choose the "bin" (or "bucket") in the first place, as we usually do in Altair, the powerful build-in function of plot_histo can automatically judge the appropriate size of each interval. 
  
- **Drawing bar plot**
  Being different from a histogram, a bar graph is a pictorial representation of data that uses bars to compare different categories of data. Bar plots are doing comparisons of discreet variables, thus, the function 'plot_bar' takes the categorical data -- users can simply specify only one categorical column in a dataframe as the only parametre, in this case, the function would count the repeatings of every value of the categorical variable and lable them as in the height of bars. Otherwise, users can specify another column as the input of the y axis.
  
- **Drawing scatter plot**
  - In a scatter plot, the data are displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.
  - A scatter plot can suggest various kinds of correlations between 2 variables. For example, weight and height, weight would be on y axis and height would be on the x axis. Correlations may be positive (rising), negative (falling), or null (uncorrelated).
  - In PlotEasy, the function plot_scatter can take in 3 parametres: the dataframe and its 2 variable (indexed by the column name).
  
  
There are some packages that provide similar functionality in the Python ecosystem. A few of the more popular packages include:

- [Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling)
- [Altair](https://pypi.org/project/altair/)

However, these packages are more oriented to skilled developers and lacking intuitive coding style. As a result, we come up with this beginner-friendly tool which helps those who are not familiar with those complex though powerful packages to embark on the EDA world confidently!


## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ ploteasy
```

## Features

- TODO

## Dependencies

- TODO

## Usage

- TODO

## Documentation

The official documentation is hosted on Read the Docs: https://ploteasy.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/fei-chang/ploteasy/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

