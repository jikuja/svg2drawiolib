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

```
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

* TBD: link to raw xml
* TBD: URL-encoded link to add library into draw.io

## Azure Icons for Draw.io

* TBD: links to raw xml
* TBD: URL-encoded links to add library into draw.io

Or all in one bundle:

* TBD: link to raw xml
* TBD: URL-encoded link to add library into draw.io
