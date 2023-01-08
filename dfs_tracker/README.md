#### Tracking DFS Results with Python using Plotly
---
This is the source code for my [Tracking DFS Results with Python using Plotly](https://ericbernier.com/dfs-tracker) blog post. This post assumes you have [Python 3 installed](https://realpython.com/installing-python/), as well as [pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv). Please read the post for further details.


##### Installation and Running the Project
Install all necessary packages and activate your virtualenv via the following commands:

```bash
pipenv install --dev
pipenv shell
```

Once your virtualenv has been activated run the command-line interface built in this post via the following command:

```bash
python dfs_tracker/tracker.py --files=csv_data/
```

##### Formatting
Format your code via the following command:

```bash
pipenv run black .
```