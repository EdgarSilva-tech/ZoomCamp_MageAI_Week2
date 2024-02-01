import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)

    """
    # Specify your transformation logic here
    print(f"Before: {print(data.isin([0]).sum())}")
    data = data[(data["passenger_count"] > 0) & (data["trip_distance"] > 0)]
    print(data.isin([0]).sum())
    print(f"Original column names: {data.columns}")
    data.columns = (data.columns
                    .str.lower()
                    .str.replace(' ', '_')
    )

    print(f"New column names: {data.columns}")
    print(data["vendorid"].value_counts())
    data['lpep_pickup_date'] = pd.to_datetime(data["lpep_pickup_datetime"]).dt.date

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert output['vendorid'].all() in [1, 2], "Not all values are in the expected range"
    #assert output['passenger_count'].isin([0]).sum() > 0, "There are zero values in passenger_count"
    #assert output['trip_distance'].isin([0]).sum() > 0, "There are zero values in trip_distance"