import pandas as pd
import altair as alt
import warnings
import altair

def plot_scatter(df, x, y):
    """Takes a dataframe and returns an altair object with scatterplot of chosen numeric features in the dataset.
    Parameters
    -----------
    df: pd.DataFrame
        The dataframe used to create a scatterplot

    X : string
        User must specify a numerical column
        
    Y : string, optional
        User can specify another numerical column
        
    Returns
    -------
    plot : altair.Chart object
        An altair plot object displaying scatterplot.
        
    Examples
    -------
    >>> example = pd.DataFrame({'name': ['Jingjing', 'Fei', 'Mengyuan'],
                                    'grade': [87, 90, 95],
                                    'hours_study': [40, 30, 20],
                                    'hours_exercise': [1, 3, 5]})
    >>> ploteasy.plot_scatter(example)
    """
    pass


def plot_bar(df,x,y):
    """Takes a dataframe with configurations and returns an altair object with summary metrics.
    Parameters
    -----------
    df: pd.DataFrame
        Dataframe from which to take columns limited to numerical columns only
    X : string
        User must specify a numerical column
    Y : string, optional
        User can specify another numerical column, by default the y lab shows the numerical information of X
   
    Returns
    -------
    plot : altair.Chart object
        An altair bar plot object displays relevant numerical information of X(and Y).

    Examples
    -------
    >>> example_df = pd.DataFrame({'student_id': [10000, 10001, 10002, 10003],
                                    'gender': ['female', 'male', 'male', 'female'],
                                    'department': ['statistics', 'biology', 'art', 'movie'],
                                    'age': [21, 23, 22, 21]})
    >>> plot_bar(example_df,gender)

"""

def plot_hist(df, density = False, title = "Histogram", exclude = []):
    """Takes a dataframe and returns a list of altair objects as histograms of all numerical features in the dataset.
    Parameters
    -----------
    df: pd.DataFrame
        The dataframe to create the histogram plot.
    density: boolean, optional
        A boolean value indicating whether or not to show the density on the histogram. 
    exclude: list, optional
        A list of strings containing the name of features that the user does not want view in the summary.
    title : string, optional
        The title of the altair plot, default title as 'Histogram'.
    Returns
    -------
    dictionary : a dictionary of altair.Chart objects
        A dictionary of altair plot objects displaying histograms of all numerical features in the dataset.
    Examples
    -------
    >>> example_df = pd.DataFrame({'student_id': [10000, 10001, 10002, 10003],
                                    'gender': ['female', 'male', 'male', 'female'],
                                    'department': ['statistics', 'biology', 'art', 'movie'],
                                    'age': [21, 23, 22, 21]})
    >>> ploteasy.plot_hist(example_df)
    """
    
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The input should be a valid dataframe.")
    if not isinstance(density, bool):
        raise TypeError("The 'density' option should be one of the boolean types: True or False.")
    if not isinstance(exclude, list):
        raise TypeError("The 'exclude' option should be a valid list of columns to be excluded.")
    
    df_numeric = df._get_numeric_data()
    showing_col = df_numeric.drop(columns = exclude)
    if len(showing_col.columns) == 0:
        warnings.warn("No valid column to plot histogram. Please check the input dataframe")
    plot_dic = {}
    
    for each in showing_col.columns:
        if density:
            plot = alt.Chart(showing_col).transform_density(
                each, as_=[each, 'density']
            ).mark_area().encode(
                x = each,
                y ='density:Q',
            )
        else:
            plot = alt.Chart(showing_col).mark_bar().encode(
                alt.X(each, bin=True),
                y='count()',
            )
        plot_dic[each] = plot
    
    return plot_dic