# streamlit_pygwalker_app

Runs PyGWalker on Stramlit.

## Requirements

* macOS or Linux
* Python: 3.10

### Library

* Poetry
* Polars
* Streamlit
* PyGWalker

## Setup

Execute following command:

```sh
git clone https://github.com/k-nai/streamlit_pygwalker_app.git
cd streamlit_pygwalker_app
```

If you use poetry, execute following command:

```sh
pip install -U pip
pip install poetry
poetry run pip install -U pip setuptools
poetry run streamlit run streamlit_app.py
```

If you don't use poetry, execute following command:

```sh
pip install -U pip
pip install -r requirements.txt
streamlit run streamlit_app.py
```

After running, your browser will launch and you will be able to use PyGWalker.  
If it does not launch, go to http://localhost:8501.

## Resources

* https://github.com/Kanaries/graphic-walker
* https://github.com/Kanaries/pygwalker