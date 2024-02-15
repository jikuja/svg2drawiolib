# svg2drawiolib

Python CLI tool to convert SVG files to draw.io shape library

## Usage

```bash
python3 src/app.py --help
```

or

```bash
svg2drawiolib --help
```

```text
usage: app.py [-h] [--mode {data,xml}] [--output OUTPUT] [--style STYLE] [--width WIDTH]
              [--height HEIGHT] [--prefix PREFIX] [--dirtitle] [--log-level LOG_LEVEL]
              [input ...]
```

### input parameters

Input parameter is one or more directories or file globs patterns.

* For input directories built-in file discovery finds recursively all SVG file(`glob.iglob(directory + '/**/*.svg', recursive=True)`)
* For files and glob pattern file discory runs recursive glob(`glob.iglob(x, recursive=True)`)

## Projects using this tool

### MSFT glyphs for Draw.io

SVG source:

* <https://azure.microsoft.com/en-gb/patterns/styles/glyphs-icons/>
* also known as Azure.microsoft.com UX Patterns
* Note: some of the icons are missing because link to SVG return 404
  * This will be fixed by parsing SVG information from the HTML

Shape library:

* [Download shape library XML file](https://raw.githubusercontent.com/jikuja/drawio-icons-msft-sundog/master/MSFT-bluedog.xml)
* [Add to Draw.io](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjikuja%2Fdrawio-icons-msft-sundog%2Fmaster%2FMSFT-bluedog.xml)

## Azure Icons for Draw.io by David Summers

SVG source/documentation/sponsor links:

* <https://github.com/David-Summers/Azure-Design>
* One of the best Azure icons collections

Download shape library XML file:

* [AI](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-AI.xml)
* [Application](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Application.xml)
* [Compute](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Compute.xml)
* [Data](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Data.xml)
* [Deployment](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Deployment.xml)
* [Endpoint](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Endpoint.xml)
* [Generic](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Generic.xml)
* [Identity](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Identity.xml)
* [IoT](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-IoT.xml)
* [Management](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Management.xml)
* [Networking](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Networking.xml)
* [Office](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Office.xml)
* [Security](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Security.xml)
* [Storage](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-Storage.xml)
* [WorkLoad](https://github.com/jikuja/drawio-icons-DS-Azure-Design/raw/master/DS-WorkLoad.xml)

Add to Draw.io

* [AI](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-AI.xml)
* [Application](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Application.xml)
* [Compute](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Compute.xml)
* [Data](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Data.xml)
* [Deployment](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Deployment.xml)
* [Endpoint](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Endpoint.xml)
* [Generic](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Generic.xml)
* [Identity](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Identity.xml)
* [IoT](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-IoT.xml)
* [Management](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Management.xml)
* [Networking](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Networking.xml)
* [Office](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Office.xml)
* [Security](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Security.xml)
* [Storage](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Storage.xml)
* [WorkLoad](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-WorkLoad.xml)

Or all in one bundle:

* [Add to Draw.io](https://app.diagrams.net/?splash=0&clibs=;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-AI.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Application.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Compute.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Data.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Deployment.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Endpoint.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Generic.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Identity.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-IoT.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Management.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Networking.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Office.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Security.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-Storage.xml;Uhttps%3A%2F%2Fgithub.com%2Fjikuja%2Fdrawio-icons-DS-Azure-Design%2Fraw%2Fmaster%2FDS-WorkLoad.xml)
