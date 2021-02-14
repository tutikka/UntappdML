# UntappdML

UntappdML is a project to export and use your personal beer history from <a href="https://untappd.com">Untappd</a> and try to apply a machine learning model to predict if you will like a new beer or not.

## Requirements

- `Python 3`
- `JupyterLab`
- `ngrok` (optional)

## Model

The machine learning model is trained, tested and persisted under the `model` directory. Everything can be done using `JupyterLab`.

You can find the example to train a `random forest classifier` int the <a href="https://github.com/tutikka/UntappdML/blob/master/model/untappd.ipynb">untappd.ipynb</a> notebook.

## Server

The server hosting the model is found under the `application`directory. The following steps can be used to start up the server.

1. Install requirements (one time)

   - `pip3 install sklearn` (scikit-learn, for the machine learning)
   - `pip3 install Flask` (backend to serve the model)
   - `pip3 install joblib` (save/load model to disk)

2. Start up the server using the `server.sh` shell script

## User Interface

The sample web user interface is used to input information on the new beer, and use that against the server to make the prediction. On your local machine, you can see the UI using a browser:

<a href="http://localhost:5000">http://localhost:5000</a>

![Image](https://github.com/tutikka/UntappdML/blob/master/screenshots/screenshot.png)

If you want to test and expose your local server to the Internet, you can use <a href="https://ngrok.com">ngrok</a>. While your server is running, run the following command in a new terminal:

`./ngrok http http://localhost:5000 -host-header="http://localhost:5000"`

You should be able to see the public URLs, for example:

```
Forwarding                    http://ae19c1fcdf17.ngrok.io -> http://localhost:5000  
Forwarding                    https://ae19c1fcdf17.ngrok.io -> http://localhost:5000
```

You can use either of these to access the UI from the Internet, for example using a tablet or mobile device.