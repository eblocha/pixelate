# Pixelate

This is a simple script that will transform an image like this:

![Python Logo](images/py-small.png)

Into text in your terminal like this:

![Python Logo](images/py-pixelated.png)

## Usage

Clone this repository and set up your virtual environment

```
python -m venv env
source env/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Print an image

```
python -m pixelate images/py.png --resize 15x15 --resampling nearest
```
