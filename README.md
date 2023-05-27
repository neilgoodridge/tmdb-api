# TMDB linked website using an API.

To get this to working, please visit https://developer.themoviedb.org/docs/getting-started and sign up for an account.

Go to your account settings and register for an API key - this is free (it's around 30 numbers and letters).

Create a new file called ```api_key.py``` in the root directory of this app. 

In there, create a variable called ```API_KEY = 'paste_your_api_key_here'```. The api_key.py file is already gitignored, so it won't push to Github.

**NOTE: Your API key will print into the terminal when first running this app. This is just to verify that it is working and has been imported correctly. Run ```python3 app.py``` and you should see your API printed in the terminal.
Comment out line 10 in app.py once you've verified it's present.**

If you do not see your API key printed, please revisit the instructions above.

Once the above is confirmed working, run the following in your terminal to run the Flask app, you can visit the site to see it in action [here](http://127.0.0.1:5000/)

```
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install Flask
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```

