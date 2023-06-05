# streamlit_pygwalker_app

Runs PyGWalker on Stramlit.

![](https://storage.googleapis.com/zenn-user-upload/bc82ad2a0378-20230407.png)

## Requirements

* macOS or Linux
* Python: 3.10

### Library

* Poetry
* pandas
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
poetry install
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
