from locust import HttpLocust, TaskSet, task
import json

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        self.client.get("/securesync/login")
        data = {"username":"abhishekc10","password":"abhishekc10","facility":"0dfa017411f05f7eb158fc465690b0fb"}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self.client.post("/securesync/api/user/login/",  data=json.dumps(data), headers=headers)

    def static(self):
        self.client.get("/static/css/jquery-ui/jquery-ui.min.css")
        self.client.get("/static/css/bootstrap-alerts.css")
        self.client.get("/static/css/distributed/khan-site.css")
        self.client.get("/static/css/distributed/khan-lite.css")
        self.client.get("/static/css/distributed/search_autocomplete.css")
        self.client.get("/_generated/dynamic.css")
        self.client.get("/static/js/json2.js")
        self.client.get("/static/js/i18n/en.js")
        self.client.get("/_generated/dynamic.js")
        self.client.get("/static/js/jquery-1.9.1.min.js")
        self.client.get("/static/js/underscore-min.js")
        self.client.get("/static/js/backbone.js")
        self.client.get("/static/js/jquery.ui.autocomplete.html.js")
        self.client.get("/static/js/modernizr.js")
        self.client.get("/static/js/handlebars/handlebars-v1.3.0.js")
        self.client.get("/static/js/khan-lite.js")
        self.client.get("/static/js/handlebars/handlebars-helpers.js")
        self.client.get("/static/js/handlebars/handlebars-wrapper.js")
        self.client.get("/static/js/distributed/user/views.js")
        self.client.get("/static/js/distributed/distributed-server.js")
        self.client.get("/static/js/distributed/search_autocomplete.js")
        self.client.get("/securesync/api/user/status")

    def index_static(self):
        self.client.get("/static/css/distributed/homepage.css")
        self.client.get("/static/js/jquery.dotdotdot.min.js")
        self.client.get("/static/js/playlist/models.js")
        self.client.get("/static/js/distributed/homepage_playlists.js")
        self.client.get("/handlebars/templates/playlists.js")

    def exercise_static(self):
        self.client.get("/handlebars/templates/exercise.js")
        self.client.get("/static/khan-exercises/css/khan-exercise.css")
        self.client.get("/static/js/seedrandom.min.js")
        self.client.get("/handlebars/templates/user.js")
        self.client.get("/static/js/distributed/software-keyboard.js")
        self.client.get("/static/js/distributed/exercises.js")
        self.client.get("/static/khan-exercises/khan-exercise.js")

    @task(1)
    def index(self):
        self.static()
        self.index_static()
        self.client.get("/")

    @task(2)
    def load_exercise(self):
        self.static()
        self.exercise_static()
        self.client.get("/static/khan-exercises/third_party/MathJax/2.1/MathJax.js?config=KAthJax-da9a7f53e588f3837b045a600e1dc439")
        self.client.get("/static/khan-exercises/exercises/addition_1.html")
        self.client.get("/math/arithmetic/addition-subtraction/basic_addition/e/addition_1")
        self.client.get("/api/exercise/addition_1")
        # TODO : Fix it
        # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        # data = ["subtraction_1"]
        # self.client.post("/api/get_exercise_logs?lang=en", data=json.dumps(data), headers=headers)
        self.client.get("/api/exerciselog/?exercise_id=addition_1&user=22d5987a7dc2553ca3a1d13b19a83f61")
        self.client.get("/api/attemptlog/?user=22d5987a7dc2553ca3a1d13b19a83f61&limit=10&exercise_id=addition_1&context_type__in=playlist&context_type__in=exercise")

    @task(3)
    def answer_exercise(self):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {"exercise_id":"addition_1","user":"/securesync/api/user/22d5987a7dc2553ca3a1d13b19a83f61/","context_type":"exercise","context_id":"","language":"","version":"0.13.0","seed":128,"complete":True,"points":20,"response_count":1,"response_log":"[{\"type\":\"loaded\",\"timestamp\":\"2015-04-10T13:24:15.388\"},{\"type\":\"answer\",\"answer\":\"12\",\"correct\":true,\"timestamp\":\"2015-04-10T13:24:20.116\"}]","timestamp":"2015-04-10T13:24:15.388","correct":True,"answer_given":"12","time_taken":4728}
        self.client.post("/api/attemptlog/", data=json.dumps(data), headers=headers)
        data = {"attempts":5,"attempts_before_completion":5,"complete":True,"completion_counter":None,"completion_timestamp":"2015-04-10T13:35:39.940","counter":None,"deleted":False,"exercise_id":"addition_1","id":"8bb71e42654258c6ba78fa976526a8f4","language":None,"points":100,"resource_uri":"/api/exerciselog/8bb71e42654258c6ba78fa976526a8f4/","signature":None,"signed_version":1,"streak_progress":100,"struggling":False,"user":"/securesync/api/user/22d5987a7dc2553ca3a1d13b19a83f61/"}
        self.client.put("/api/exerciselog/8bb71e42654258c6ba78fa976526a8f4/", data=json.dumps(data), headers=headers)
        self.client.get("/api/exerciselog/?exercise_id=addition_1&user=22d5987a7dc2553ca3a1d13b19a83f61")
        self.client.get("/api/attemptlog/?user=22d5987a7dc2553ca3a1d13b19a83f61&limit=10&exercise_id=addition_1&context_type__in=playlist&context_type__in=exercise")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000
