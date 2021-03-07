from ploteasy import __version__
from ploteasy import ploteasy
import pandas as pd
import altair as alt
from vega_datasets import data


def test_version():
    assert __version__ == '0.1.0'

def input_df():    
    df = data.movies()
    return df

def test_input_df(input_df):
    rows_in_df = len(input_df)
    assert rows_in_df == 3201

def test_plot_basic_distributions(input_df):
    
    # Tests on input:
    with pytest.raises(TypeError) as exc_info:
        ploteasy.plot_hist('Not a dataframe')     
    assert 'The input should be a valid dataframe' in str(exc_info.value) 
    
    with pytest.raises(TypeError) as exc_info:
        ploteasy.plot_hist(input_df, density= 'Not a boolean')  
    assert 'should be one of the boolean types: True or False' in str(exc_info.value)  
    
    with pytest.raises(TypeError) as exc_info:
        ploteasy.plot_hist(input_df, exclude = 'Not a list')  
    assert 'should be a valid list of columns to be excluded' in str(exc_info.value)     

    with pytest.warns(UserWarning) as exc_info:
        # Excluding all columns from the input dataframe will cause no plot being generated.
        ploteasy.plot_hist(input_df, exclude= input_df.columns) 
    assert ''      

    # Tests on output 
    dict_plots = ploteasy.plot_hist(input_df)
    assert len(dict_plots.keys()) == 8
    assert list(dict_plots.keys()) == ['US_Gross', 'Worldwide_Gross', 'US_DVD_Sales', 'Production_Budget', 'Running_Time_min', 'Rotten_Tomatoes_Rating', 'IMDB_Rating', 'IMDB_Votes']

    for key in dict_plots.keys():
        assert isinstance(dict_plots[key], alt.Chart)