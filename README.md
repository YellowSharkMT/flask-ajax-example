# Flask Ajax Example

This is an example app that uses Flask-WTF and AJAX. There are two versions of the frontend: one uses jQuery, the other uses AngularJS.

1.) Create a new virtualenv and run `pip install -r requirements.txt`.

2.) Run the app: `python flask-manage.py`

3.) Open your browser to http://127.0.0.1:5000 to view the app.

The `flask-ajax.py` file contains all python code, and the frontend code for the jQuery version is contained in the `templates/home.html` file, while the frontend code for the AngularJS version is in the `templates/home-angular.html` file.

Note that the AngularJS version requires the [`http-post-fix`](https://gist.github.com/JensRantil/5713606) module in order to correct the format for POST-ed data. 