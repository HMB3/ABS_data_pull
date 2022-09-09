# SpaceCruch
# Fri 09/09/2022
# Description: Downloads GeoPackages Census data from ABS website.
# A list of all geopackage topics and tables are avaiable for download at the link below:
# See: https://www.abs.gov.au/census/guide-census-data/about-census-tools/geopackages

import re
import requests
from os.path import basename
from pathlib import Path
from urllib.parse import urljoin
from dataclasses import dataclass


@dataclass
class ABSGeopackagesDownloader:
    abs_geopackages_url = 'https://www.abs.gov.au/census/find-census-data/geopackages'
    abs_homepage_url = 'https://www.abs.gov.au'
    states = [
        # "AUST",
        "ACT",
        "NSW",
        "NT",
        "OT",
        "QLD",
        "SA",
        "TAS",
        "VIC",
        "WA",
    ]

    def extract_download_link(self):
        print('Finding files...')
        html = requests.get(self.abs_geopackages_url)
        for cap in re.finditer(f"href=([\w/-]+_({'|'.join(self.states)})_GDA2020.zip)", html.text):
            yield cap[1]

    def download_files(self, dirpath):
        file = Path(basename(dirpath))
        if file.exists():
            print(f'{file.name} already exists.')
            return
        dlink = urljoin(self.abs_homepage_url, dirpath)
        print(f'Downloading: {file.name}', end="... ")
        req = requests.get(dlink)
        if req.ok:
            file.write_bytes(req.content)
            print("OK")
        else:
            print("ERROR")

    def download(self):
        for link in self.extract_download_link():
            self.download_files(link)


if __name__ == "__main__":
    geopackages = ABSGeopackagesDownloader()
    geopackages.download()
