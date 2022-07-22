# translate-this-keywords-for-me

This repository contains a short python script that translates CiteSpace's exported keywords into whatever language you choose. 

## Installation

```console
$ git clone https://github.com/hcss-utils/translate-this-keywords-for-me.git
$ cd translate-this-keywords-for-me
$ python3 -m venv env
$ . env/bin/activate
(env)$ pip install -r requirements.txt
```

## Usage

Run the script with `--help` to see possible options and positional arguments: 
```console
>>> python translate.py --help
usage: translate.py [-h] [--source-lang SOURCE_LANG] [--target-lang TARGET_LANG]
                    input output

Translate keywords.

positional arguments:
  input                 Input file name
  output                Output file name

options:
  -h, --help            show this help message and exit
  --source-lang SOURCE_LANG, -src SOURCE_LANG
  --target-lang TARGET_LANG, -tg TARGET_LANG
```

Real life example: translate [`keywords_zh`](assets/keywords_zh.csv) from Chinese to English
```
python translate.py assets/keywords_zh.csv assets/keywords_zh_en.csv -src=zh-cn -tg=en
```