# ABS_data_pull
Repo for pulling all ABS data down


The ABS has a BETA API for getting data :

https://api.gov.au/assets/APIs/abs/DataAPI.openapi.html

Looks like the spatial data is not available through SQL-style requests (yet).
Somewhat incredulous, but lots of people must be requesting it....

https://www.abs.gov.au/census/find-census-data/census-data-tools

## ABS GeoPackage Downloader - Notes

File contains a list of states - comment to include/exclude in the downloads list. The Australia-wide datasets are large and is commented out by default. I am thinking
it is preferrable to keep the data separated into smaller state chunks for easier loading and processing.

Usage:

```bash
# Usage

cd $dirname
python abs_census_geopackages_downloader.py
```
