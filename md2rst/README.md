# README
## Prerequisite
You should install `pandoc` on your machine first.
- Official Website: [Install Pandoc](https://pandoc.org/installing.html)

## Usage
```shell
python md2rst.py [src_file] [dst_file]
```

## Test

You can test with the following script to see whether rst is transformed.

```shell
python md2rst.py README.md README.rst
```



## Change Log

- **V0.0.1**
	- support the transformation of **single** markdown file
	- support transformation through a  `web API` and `pandoc`

## TODO

- [ ] add  --help
- [ ] support multi-transformation, directory-transformation
- [ ] support multi-thread
- [ ] support auto-generation for index.rst **(Important)**