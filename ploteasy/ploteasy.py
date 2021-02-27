
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


def plot_hist(df, density = False, title = "Histogram", exclude = []):
    """Takes a dataframe and returns an altair object with histograms of all categorical features in the dataset.
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
    plot : altair.Chart object
        An altair plot object displaying histograms of all categorical features in the dataset.
    Examples
    -------
    >>> example_df = pd.DataFrame({'student_id': [10000, 10001, 10002, 10003],
                                    'gender': ['female', 'male', 'male', 'female'],
                                    'department': ['statistics', 'biology', 'art', 'movie'],
                                    'age': [21, 23, 22, 21]})
    >>> ploteasy.plot_hist(example_df)

    """
    pass