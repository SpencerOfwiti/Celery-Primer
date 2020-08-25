# Celery-Primer 
An intro to using celery for implementing task queues. 

## Table of contents
* [Built With](#built-with)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Authors](#authors)

## Built With
* [Python 3.6](https://www.python.org/) - The programming language used.
* [Celery](https://docs.celeryproject.org/en/stable/index.html) - The distributed task queue framework used. 
* [Redis](https://redis.io/) - The message broker used. 

## Prerequisites

What things you need to install the software and how to install them

* **python 3**

Linux:
```
sudo apt-get install python3.6
```

Windows:

Download from [python.org](https://www.python.org/downloads/windows/) 

Mac OS:
```
brew install python3
```

* **pip**

Linux and Mac OS:
```
pip install -U pip
```

Windows:
```
python -m pip install -U pip
```

## Installation

Clone this repository:
```
git clone https://github.com/SpencerOfwiti/Celery-Primer 
```

To set up virtual environment and install dependencies:
```
python3 - m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run celery worker server:
```
celery -A proj worker --loglevel=info
```

To run python scripts:
```
python3 main.py
```

To run tests:
```
pytest 
```

## Authors

* **[Spencer Ofwiti](https://github.com/SpencerOfwiti)** - *Initial work* 
    
[![github follow](https://img.shields.io/github/followers/SpencerOfwiti?label=Follow_on_GitHub)](https://github.com/SpencerOfwiti)
[![twitter follow](https://img.shields.io/twitter/follow/SpencerOfwiti?style=social)](https://twitter.com/SpencerOfwiti)

