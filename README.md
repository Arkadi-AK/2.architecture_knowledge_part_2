Installation
* `pip install behave`
* `cd bdd_behave`
* `behave -i features/zero_test.feature`

Project Structure
```angular2html
[project root directory]
|‐‐ [product code packages]
|-- features
|   |-- environment.py
|   |-- *.feature
|   `-- steps
|       `-- *_steps.py
`-- [behave.ini|.behaverc|tox.ini|setup.cfg]
```
