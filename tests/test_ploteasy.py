from ploteasy import __version__
from ploteasy import ploteasy
import altair as alt
import pytest
from vega_datasets import data


def test_version():
    assert __version__ == '0.1.0'


def load_input_df():
    input_df = data.movies()
    return input_df


def test_input_df():
    input_df = data.movies()
    rows_in_df = len(input_df)
    assert rows_in_df == 3201


def test_plot_basic_distributions():
    input_df = data.movies()
    # Tests on input:
    with pytest.raises(TypeError) as exc_info:
        ploteasy.plot_hist('Not a dataframe')
    assert 'Should Dataframe' in str(exc_info.value)
    with pytest.raises(TypeError) as exc_info:
        ploteasy.plot_hist(input_df, density='Not a boolean')
    assert 'Should be boolean' in str(exc_info.value)
    with pytest.raises(TypeError) as exc_info:
        ploteasy.plot_hist(input_df, exclude='Not a list')
    assert 'Should be a valid list' in str(exc_info.value)
    # Tests on output
    dict_plots = ploteasy.plot_hist(input_df)
    assert len(dict_plots.keys()) == 8
    assert list(dict_plots.keys()) == ['US_Gross', 'Worldwide_Gross',
                                       'US_DVD_Sales', 'Production_Budget',
                                       'Running_Time_min',
                                       'Rotten_Tomatoes_Rating',
                                       'IMDB_Rating',
                                       'IMDB_Votes']
    for key in dict_plots.keys():
        assert isinstance(dict_plots[key], alt.Chart)
