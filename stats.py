#!/usr/bin/env python3
'''
Script using various `descriptive statistical`_ methods for analysing solar
energy data.

Script accepts `.json` file, as output by :mod:`energy` script.

.. _descriptive statistical: https://en.wikipedia.org/wiki/Descriptive_statistics

'''
# Standard imports
from typing import Tuple

# Third-party imports
import pandas as pd
import plac


def get_energy_dataframe(df: pd.DataFrame) -> Tuple[pd.DataFrame, str, str]:
    '''
    From the given ``energy`` pandas dataframe extract the ``timeUnit``,
    ``unit`` and ``values`` data.

    :return: Tuple containing 3 items:
        [1] Pandas dataframe containing the energy values,
        [2] Time unit of the energy data,
        [3] Energy value units
    :rtype: Tuple[pd.DataFrame, str, str]

    '''
    time_unit = df['energy']['timeUnit']
    energy_unit = df['energy']['unit']
    energy_df = pd.DataFrame(df['energy']['values'])
    return energy_df, time_unit, energy_unit


def time_unit_stats_day(df: pd.DataFrame, time_unit: str, energy_unit: str) -> None:
    '''
    Display various statistics relevant when energy data collected using
    ``TimeUnit`` of ``DAY``.

    :param df: DataFrame containing energy data values.
    :type df: pd.DataFrame
    :param time_unit: The time unit of the energy data.
    :type time_unit: str
    :param energy_unit: The unit of the energy data.
    :type energy_unit: str
    '''
    if time_unit != "DAY":
      return

    big_days_value = 30000
    big_days = df.loc[df['value'].transform(lambda x: x.ge(big_days_value))]
    print(f"{len(big_days)} {time_unit}{'s'[:len(big_days)^1]} over " +\
          f"{big_days_value} {energy_unit}:\n{big_days}")

    little_days_value = 500
    little_days = df.loc[df['value'].transform(lambda x: x.le(little_days_value))]
    print(f"{len(little_days)} {time_unit}{'s'[:len(little_days)^1]} below " +\
          f"{little_days_value} {energy_unit}:\n{little_days}")


@plac.pos('data_file', ".json file containing energy data", type=str)
def __main(data_file: str) -> None:
    '''
    Read engery data from supplied `.json` file (created using `energy` script)
    and output various statistics.
    '''

    json_df = pd.read_json(data_file)
    # Does the read .json file contain energy data
    if 'energy' not in json_df:
        print(f"File {data_file} does not contain 'energy' data")
        return

    energy_df, time_unit, energy_unit = get_energy_dataframe(json_df)

    max_entry = energy_df.loc[energy_df['value'].idxmax()]
    min_entry = energy_df.loc[energy_df['value'].idxmin()]

    #print(energy_df)
    print(f"{time_unit} most energy is {max_entry['date']}: " \
          f"{max_entry['value']} {energy_unit}")
    print(f"{time_unit} least energy is {min_entry['date']}: " \
          f"{min_entry['value']} {energy_unit}")

    time_unit_stats_day(energy_df, time_unit, energy_unit)


if __name__ == '__main__':
    plac.call(__main)

# end-of-file
