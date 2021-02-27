def plot_bar(df,x,y):
    """Takes a dataframe with configurations and returns an altair object with summary metrics.
    Parameters
    -----------
    df: pd.DataFrame
        Dataframe from which to take columns limited to numerical columns only
    X : string
        User must specify a numerical column
    Y : string, optional
        User can specify another numerical column, by default the y lab shows the 		numerical information of X
   
    Returns
    -------
    plot : altair.Chart object
        An altair bar plot object displays relevant numerical information of X(and Y).

    Examples
    -------
    >>> example_df = pd.DataFrame({'animal': ['falcon', 'dog', 'spider', 'fish'],
                                    'num_legs': [2, 4, 8, 0],
                                    'num_wings': [2, 0, 0, 0],
                                    'num_specimen_seen': [10, 2, 1, 8]})
    >>> plot_bar(example_df,animal,num_legs)
    """
    pass