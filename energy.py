'''
Use the SolarEdge Monitoring API ``energy`` command to get engery generation data.
'''

# Standard imports
import os
import traceback
from typing import Tuple

# Third-party imports
import plac
import requests
import yaml

def load_site_api_data(file_name: str = 'site_api_key.yaml') -> Tuple[str, str]:
    '''
    '''
    site_api_data = {}
    with open(file_name, "r") as stream:
        try:
            site_api_data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise yaml.YAMLError("Cannot read site api data from file "
                                 f"'{file_name}'") from exc

    if 'site_id' not in site_api_data or 'api_key' not in site_api_data:
        raise RuntimeError(f"File '{file_name} must contain keys 'site_id' and "
                           f"'api_key'. File contents: '{site_api_data}'")

    return site_api_data['site_id'], site_api_data['api_key']


def get_energy_data(site_id: str, api_key: str,
                    start_date: str, end_date: str, time_unit):
    '''
    '''
    api_cmd= "energy?"
    url = f"https://monitoringapi.solaredge.com/site/{site_id}/{api_cmd}"

    api_params = {"timeUnit": time_unit,
                  "startDate": start_date,
                  "endDate": end_date,
                  "api_key": api_key}

    response = requests.get(url, params=api_params, timeout=3.0)
    print(f"Request URL: {response.url}")

    data_file_name = f"data/energy_{start_date}_to_{end_date}_{time_unit}.json"
    with open(data_file_name, "w") as data_file:
        data_file.write(response.text)
    print(f"Energy data written to '{data_file_name}'")


@plac.pos('start_date', "Start date, e.g. '2021-08-01'", type=str)
@plac.pos('end_date', "End date, e.g. '2021-08-31'", type = str)
@plac.opt('time_unit', "Time unit, one of 'QUARTER_OF_AN_HOUR', 'HOUR', " \
          "'DAY', 'WEEK', 'MONTH', or 'YEAR'", type=str,
          choices=['QUARTER_OF_AN_HOUR', 'HOUR', 'DAY', 'WEEK', 'MONTH', 'YEAR'])
@plac.opt('site_data', "Name of .yaml file containing site data", type=str)
def main(start_date: str, end_date: str, time_unit: str = 'QUARTER_OF_AN_HOUR',
         site_data: str = 'site_api_key.yaml') -> None:
    '''
    Call the SolarEdge Monitoring API `energy` command to get engery generation
    data and store in `.json` file.
    '''
    site_id, api_key = load_site_api_data(site_data)

    get_energy_data(site_id, api_key, start_date, end_date, time_unit)


# end main()

if __name__ == '__main__':
    try:
        plac.call(main)
    except Exception as main_exc:
        print("Exception executing " + os.path.basename(__file__) +
              f" main() Exception: {main_exc}")
        print(traceback.format_exc())

# end-of-file
