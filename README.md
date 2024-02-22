# edi\_triage

Untersuchung von Dateien zur frühen Erkennung von potentiellem Schadcode

## Installation

```
mkdir my-project
cd my-project
git clone https://github.com/educorvi/edi-triage.git
python3 -m venv venv
source venv/bin/activate
pip3 install -e edi-triage
```

## Test

```
% python3
Python 3.10.13 (main, Aug 24 2023, 12:59:26) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from edi_triage.converter.rechner import add
>>> add(3,3)
6.0
>>>
```
