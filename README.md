# My Portfolio website


👋  Hi! I'm Lenz Paul. I'm a programmer from [Vancouver, Canada](https://www.google.com/maps/place/Vancouver,+BC/@49.2576508,-123.2639868,11z/data=!3m1!4b1!4m5!3m4!1s0x548673f143a94fb3:0xbb9196ea9b81f38b!8m2!3d49.2827291!4d-123.1207375?hl=en).  

<!-- TODO: Insert the link in between the parenthesis -->
This is my portfolio deployed on Google App Engine [here]().
<br>
## The project
### Technologies used
I've used the following technologies:
- [Google App Engine](https://cloud.google.com/appengine/docs/overview)
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)

### The app
- Templated html files are located in `templates/`
- App engine configuration is located in `app.yaml` 
- The Flask code is located in `main.py`
- Images are located in `static/images/`
- My resume is located in `static/static/general_swe_resume_lenz_paul_nov_2021.pdf`

## Deployment
To deploy this app **live**:
- From a terminal, with Google Cloud SDK or from the Google Cloud Shell, run:
  ```
  gcloud app deploy
  ```

To test this app **locally**:
- From a terminal, run:
  ```
  python main.py
  ```

From a local machine:
- Create a virtual environment:
  ```
  python3 -m venv env
  ```  
- Activate the virtual environment:
    ```
    source env/bin/activate
    ```
- Install dependencies:
    ```
    pip install -r requirements.txt
    ```
- Run the app:
    ```
    python main.py
    ```
    The url for the app will be displayed in the terminal (e.g.  Running on http://127.0.0.1:5000/).