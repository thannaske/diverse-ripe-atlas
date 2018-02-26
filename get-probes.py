#!/usr/bin/env python3

import urllib.request
import json

from requests import HTTPError

COUNTRY_CODE = "DE"
API_ENDPOINT = "https://atlas.ripe.net/api/v2/probes/"

probes = {
    "asn_v4": dict(),
}

current_page = 1

while True:
    try:
        with urllib.request.urlopen(API_ENDPOINT + "?page=" + str(current_page) + "&country_code=" + COUNTRY_CODE + "&status_name=Connected") as response:
            json_response = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))

            if "next" in json_response:
                if json_response["next"] is None:
                    continue_fetching = False
                else:
                    # There are more than one result pages
                    continue_fetching = True
                    current_page += 1
            else:
                # Just one result page
                continue_fetching = False

            for r in json_response["results"]:
                asn_v4 = r["asn_v4"]
                asn_v6 = r["asn_v6"]
                probe_id = r["id"]

                if asn_v4 in probes["asn_v4"]:
                    if len(probes["asn_v4"][asn_v4]) < 2:
                        probes["asn_v4"][asn_v4].append(probe_id)
                    else:
                        pass
                else:
                    probes["asn_v4"][asn_v4] = list()
                    probes["asn_v4"][asn_v4].append(probe_id)

            if not continue_fetching:
                # Break out of the loop
                break
    except HTTPError:
        # Break out of loop
        break

output_string = ""

for _, value in probes["asn_v4"].items():
    for id in value:
        output_string += str(id) + ","

# Omit last comma
print(output_string[:-1])
