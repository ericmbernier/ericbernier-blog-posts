init: 
    pipenv install --dev

format: 
    pipenv run black football_api tests

test: 
    pytest tests

coverage: 
    pytest --cov football_api --cov-report term-missing tests