## appengine-googleanalytics-python

Integrating App Engine with Google Analytics

## Project setup, installation, and configuration

- Register for [Google Analytics](http://www.google.com/analytics/), create
an application, and get a tracking id.
- Set the `GA_TRACKING_ID` constant in `tracking.py` to the Google Analytics
tracking id of your application.

To run the test

    python test/test_runner.py SDK_PATH src test
    
Substituting `SDK_PATH` with the appengine python sdk directory, for example
`~/google-cloud-sdk/platform/google_appengine`.

## Running the demo

To build the demo, run

    build.sh build_demo

To run the demo, run

    build.sh run_demo

## Contributing changes

* See [CONTRIB.md](CONTRIB.md)

## Licensing

* See [LICENSE](LICENSE)
