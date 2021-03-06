import pandas as pd
import altair as alt
import warnings


def plot_scatter(data, x, y, color="green",
                 title=None, plot_width=300, plot_height=300):
    """Takes a dataframe and returns an altair object with
    scatterplot of chosen numeric features in the dataset.
    X : string
        User must specify a numerical column
    Y : string, optional
        User can specify another numerical column
    color : string, optional
            User can specify color of points
    title : string, optional
            User can specify title of plot
    plot_width: integer, optional
                Width of the plot.
    plot_height: integer, optional
                Height of the plot
    Returns
    -------
    plot : altair.Chart object
        An altair plot object displaying scatterplot.
    Examples
    -------
    >>> example_df = pd.DataFrame({'student_id': [10000, 10001],
                                    'gender': ['female', 'male'],
                                    'age': [21, 23]})
    >>> ploteasy.plot_scatter(example_df)
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("`data` must be entered as a pandas dataframe")
    elif not isinstance(x, str):
        raise ValueError("`x` must be a string")
    elif not isinstance(y, str):
        raise ValueError("`y` must be a string")
    elif not isinstance(color, str):
        raise ValueError("`color` must be a string")
    elif title is None:
        raise ValueError("Please enter your title")
    elif not isinstance(title, str):
        raise ValueError("`title` must be a string")
    elif not isinstance(plot_width, int):
        raise ValueError("plot_width must be an integer")
    elif not isinstance(plot_height, int):
        raise ValueError("plot_height must be an integer")
    scatter_plot = (
        alt.Chart(data, title=alt.TitleParams(text=title))
        .mark_circle(size=20, opacity=0.6, color=color)
        .encode(
            alt.X(x),
            alt.Y(y),
        ).properties(
            width=plot_width,
            height=plot_height
        ).configure_axis(
            titleFontSize=18,
            labelFontSize=12))
    return scatter_plot


def plot_bar(data, x, y, color="green",
             title=None, plot_width=300, plot_height=300):
    """Takes a dataframe and returns an altair object
    with scatterplot of chosen numeric features in the dataset.
    Parameters
    -----------
    data: pd.DataFrame
        The dataframe used to create a scatterplot
    X : string
        User must specify a numerical column
    Y : string, optional
        User can specify another numerical column
    color : string, optional
            User can specify color of points
    title : string, optional
            User can specify title of plot
    plot_width: integer, optional
                Width of the plot.
    plot_height: integer, optional
                Height of the plot
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
    >>> ploteasy.plot_bar(example)
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("`data` must be entered as a pandas dataframe")
    elif not isinstance(x, str):
        raise ValueError("`x` must be a string")
    elif not isinstance(y, str):
        raise ValueError("`y` must be a string")
    elif not isinstance(color, str):
        raise ValueError("`color` must be a string")
    elif title is None:
        raise ValueError("Please enter your title")
    elif not isinstance(title, str):
        raise ValueError("`title` must be a string")
    elif not isinstance(plot_width, int):
        raise ValueError("plot_width must be an integer")
    elif not isinstance(plot_height, int):
        raise ValueError("plot_height must be an integer")
    plot_bar = (
        alt.Chart(data, title=alt.TitleParams(text=title))
        .mark_circle(size=20, opacity=0.6, color=color)
        .encode(
            alt.X(x),
            alt.Y(y),
        ))
    return plot_bar


def plot_hist(df, density=False, title="Histogram", exclude=[]):
    """Takes a dataframe and returns a list of altair objects as
    histograms of all numerical features in the dataset.
    Parameters
    -----------
    df: pd.DataFrame
        The dataframe to create the histogram plot.
    density: boolean, optional
        A boolean value indicating whether or not to
        show the density on the histogram.
    exclude: list, optional
        A list of strings containing the name of features that
        the user does not want view in the summary.
    title : string, optional
        The title of the altair plot, default title as 'Histogram'.
    Returns
    -------
    dictionary : a dictionary of altair.Chart objects
        A dictionary of altair plot objects displaying histograms
        of all numerical features in the dataset.
    Examples
    -------
    >>> example_df = pd.DataFrame({'student_id': [10000, 10001],
                                    'gender': ['female', 'male'],
                                    'age': [21, 23]})
    >>> ploteasy.plot_hist(example_df)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Should Dataframe.")
    if not isinstance(density, bool):
        raise TypeError("Should be boolean.")
    if not isinstance(exclude, list):
        raise TypeError("Should be a valid list.")
    df_numeric = df._get_numeric_data()
    showing_col = df_numeric.drop(columns=exclude)
    if len(showing_col.columns) == 0:
        warnings.warn("No valid column to plot histogram. \
                       Please check the input dataframe")
    plot_dic = {}
    for each in showing_col.columns:
        if density:
            plot = alt.Chart(showing_col).transform_density(
                each, as_=[each, 'density']
            ).mark_area().encode(
                x=each,
                y='density:Q',
            )
        else:
            plot = alt.Chart(showing_col).mark_bar().encode(
                alt.X(each, bin=True),
                y='count()',
            )
        plot_dic[each] = plot
    return plot_dic
