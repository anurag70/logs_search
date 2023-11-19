The complete project is made in Django(for backend),for database used Postgres, for fast and optimized searching used ElasticSearch.

Ther's a api exposed for data population in db(post call->{host}/log/update)
For querying exposed api: ({host}/log/search)

To query the log have to run query from CLI:
Steps:
a. 1st run log_cli.py(python log_cli.py)
b. then for searching put input in this way(
level:error,message:....,spanId:....

)

to run this project:
---> install the requirements.txt file(pip install -r requirements.txt --use-deprecated==legacy-resolver)
