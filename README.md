# diverse-ripe-atlas
Get ASN-diverse Probe IDs of the RIPE Atlas API for meaningful measurements.

## What's this for?
When runnning measurements on RIPE's Atlas system you sometimes can't use their probe-wizard to select the diversity of probes you may need. When measuring the connectivity of a system you may want to have a widespread count of ASNs in your probe set. This script is designed to fetch all connected probes of a single country (currently hardcoded to `DE` (Germany)) and to get two probes per ASN.

Finally it prints a comma-seperated list of the resulting probe IDs that you can use in your RIPE Atlas measurement wizard.
