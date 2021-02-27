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