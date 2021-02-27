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