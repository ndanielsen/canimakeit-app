### Error Log for Using Pickle for prediction


nathan@nathan:~/Projects/canimakeit/canimakeit-app$ python server.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
127.0.0.1 - - [02/Aug/2015 12:47:22] "GET / HTTP/1.1" 200 -

Received:  {"salary":"60","":"","household-size":"1","is-rent":"false"} 


127.0.0.1 - - [02/Aug/2015 12:47:24] "POST /api/user-info HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1836, in __call__
    return self.wsgi_app(environ, start_response)
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1820, in wsgi_app
    response = self.make_response(self.handle_exception(e))
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1403, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1817, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1477, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1381, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1475, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1461, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/nathan/Projects/canimakeit/canimakeit-app/server.py", line 41, in post
    recommendation = recommender.recommend(user_salary=salary)
  File "/home/nathan/Projects/canimakeit/canimakeit-app/model/recommender.py", line 55, in recommend
    user_recommendations['state_cluster'] = self.statecluster.predict(salary=user_salary, family_size=household_size, own=own, rent=rent )
  File "/home/nathan/Projects/canimakeit/canimakeit-app/model/predict.py", line 129, in predict
    return self.log_clusters(salary=salary, family_size=family_size, own=own, rent=rent)
  File "/home/nathan/Projects/canimakeit/canimakeit-app/model/predict.py", line 120, in log_clusters
    logreg_production = pickle_loader(pickle_file)
  File "/home/nathan/Projects/canimakeit/canimakeit-app/model/predict.py", line 104, in pickle_loader
    with open(pickle_file, "r+") as fp:     #Load model from file
IOError: [Errno 2] No such file or directory: '/home/nathan/Projects/canimakeit/canimakeit-app/state/mvp_2015_0801.pickle'
