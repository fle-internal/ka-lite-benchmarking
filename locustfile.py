from locust import HttpLocust, TaskSet, task
import json
import os,binascii

USER_CREDENTIALS = [
    ("student1", "student1"),
    ("student2", "student2"),
    ("student3", "student3"),
    ("student4", "student4"),
    ("student5", "student5"),
    ("student6", "student6"),
    ("student7", "student7"),
    ("student8", "student8"),
    ("student9", "student9"),
    ("student10", "student10"),
    ("student11", "student11"),
    ("student12", "student12"),
    ("student13", "student13"),
    ("student14", "student14"),
    ("student15", "student15"),
    ("student16", "student16"),
    ("student17", "student17"),
    ("student18", "student18"),
    ("student19", "student19"),
    ("student20", "student20"),
    ("student21", "student21"),
    ("student22", "student22"),
    ("student23", "student23"),
    ("student24", "student24"),
    ("student25", "student25"),
    ("student26", "student26"),
    ("student27", "student27"),
    ("student28", "student28"),
    ("student29", "student29"),
    ("student30", "student30"),
    ("student1", "student1"),
    ("student2", "student2"),
    ("student3", "student3"),
    ("student4", "student4"),
    ("student5", "student5"),
    ("student6", "student6"),
    ("student7", "student7"),
    ("student8", "student8"),
    ("student9", "student9"),
    ("student10", "student10"),
    ("student11", "student11"),
    ("student12", "student12"),
    ("student13", "student13"),
    ("student14", "student14"),
    ("student15", "student15"),
    ("student16", "student16"),
    ("student17", "student17"),
    ("student18", "student18"),
    ("student19", "student19"),
    ("student20", "student20"),
    ("student21", "student21"),
    ("student22", "student22"),
    ("student23", "student23"),
    ("student24", "student24"),
    ("student25", "student25"),
    ("student26", "student26"),
    ("student27", "student27"),
    ("student28", "student28"),
    ("student29", "student29"),
    ("student30", "student30")
]

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        if len(USER_CREDENTIALS) > 0:
            user, password = USER_CREDENTIALS.pop()
            self.login(user,password)
        else:
            self.login("student1","student1")

    def login(self, user, password):
        self.client.get("/securesync/login")
        data = {"username":user,"password":password,"facility":"847ad21ce94c43fa91f10292744f6a37"}
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
        self.client.get("/static/khan-exercises/interface.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.core.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.widget.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.mouse.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.position.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.effect.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.effect-shake.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.button.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.draggable.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.resizable.js")
        self.client.get("/static/khan-exercises/local-only/jquery.ui.dialog.js")
        self.client.get("/static/khan-exercises/local-only/jquery.qtip.js")
        self.client.get("/static/khan-exercises/local-only/kas.js")
        self.client.get("/static/khan-exercises/local-only/jed.js")
        self.client.get("/static/khan-exercises/local-only/localeplanet/icu.en-US.js")
        self.client.get("/static/khan-exercises/local-only/katex/katex.js")
        self.client.get("/static/khan-exercises/history.js")
        self.client.get("/static/khan-exercises/interface.js")
        self.client.get("/static/khan-exercises/third_party/MathJax/2.1/MathJax.js?config=KAthJax-da9a7f53e588f3837b045a600e1dc439")
        self.client.get("/static/khan-exercises/utils/jquery.adhesion.js")
        self.client.get("/static/khan-exercises/utils/tex.js")
        self.client.get("/static/khan-exercises/utils/tmpl.js")
        self.client.get("/static/khan-exercises/utils/calculator.js")
        self.client.get("/static/khan-exercises/utils/answer-types.js")
        self.client.get("/static/khan-exercises/third_party/raphael.js")
        self.client.get("/static/khan-exercises/utils/math.js")
        self.client.get("/static/khan-exercises/utils/word-problems.js")
        self.client.get("/static/khan-exercises/third_party/MathJax/2.1/images/MenuArrow-15.png")
        self.client.get("/static/khan-exercises/third_party/MathJax/2.1/jax/output/HTML-CSS/fonts/TeX/fontdata.js")
        self.client.get("/static/khan-exercises/third_party/MathJax/2.1/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff")
        self.client.get("/static/khan-exercises/third_party/MathJax/2.1/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff")
        self.client.get("/static/khan-exercises/third_party/MathJax/2.1/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff")
        self.client.get("/static/khan-exercises/third_party/MathJax/2.1/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff")
        self.client.get("/static/js/seedrandom.min.js")
        self.client.get("/handlebars/templates/exercise.js")
        self.client.get("/static/js/distributed/software-keyboard.js")
        self.client.get("/static/js/modernizr.js")
        self.client.get("/static/khan-exercises/css/khan-exercise.css")
        self.client.get("/static/js/backbone.js")
        self.client.get("/static/js/distributed/exercises.js")
        self.client.get("/static/khan-exercises/khan-exercise.js")
        self.client.get("/securesync/api/user/status/")
        self.client.get("/static/khan-exercises/local-only/katex/fonts/fonts.css")
        self.client.get("/static/khan-exercises/local-only/katex/katex.css")
        self.client.get("/static/khan-exercises/local-only/jquery-migrate-1.1.1.js")


    @task(1)
    def index(self):
        # self.static()
        # self.index_static()
        self.client.get("/")

    @task(2)
    def load_exercise(self):
        # self.static()
        # self.exercise_static()
        response = self.client.get("/securesync/api/user/status")
        user_id = json.loads(response.text)["user_id"]
        # self.client.get("/static/khan-exercises/third_party/MathJax/2.1/MathJax.js?config=KAthJax-da9a7f53e588f3837b045a600e1dc439")
        # self.client.get("/static/khan-exercises/exercises/addition_1.html")
        # self.client.get("/math/arithmetic/addition-subtraction/basic_addition/e/addition_1")
        self.client.get("/api/exercise/addition_1")
        self.client.get("/api/exerciselog/?exercise_id=addition_1&user=" + user_id)
        self.client.get("/api/attemptlog/?user=" + user_id + "&limit=10&exercise_id=addition_1&context_type__in=playlist&context_type__in=exercise")

    @task(3)
    def answer_exercise(self):
        response = self.client.get("/securesync/api/user/status")
        user_id = json.loads(response.text)["user_id"]
        exerciselog_id = binascii.b2a_hex(os.urandom(15))
        exerciselog_url = "/api/exerciselog/" + exerciselog_id + "/"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        url  = "/securesync/api/user/" + user_id + "/"
        data = {"exercise_id":"addition_1","user":url ,"context_type":"exercise","context_id":"","language":"","version":"0.13.0","seed":82,"complete":True,"points":20,"response_count":1,"response_log":"[{\"type\":\"loaded\",\"timestamp\":\"2015-04-21T11:37:31.533\"},{\"type\":\"answer\",\"answer\":\"10\",\"correct\":True,\"timestamp\":\"2015-04-21T11:37:37.667\"}]","timestamp":"2015-04-21T11:37:31.533","correct":True,"answer_given":"10","time_taken":6134}
        self.client.post("/api/attemptlog/", data=json.dumps(data), headers=headers)
        data = {"attempts":5,"attempts_before_completion":5,"complete":True,"completion_counter":None,"completion_timestamp":"2015-04-10T13:35:39.940","counter":None,"deleted":False,"exercise_id":"addition_1","id":exerciselog_id,"language":None,"points":100,"resource_uri": exerciselog_url,"signature":None,"signed_version":1,"streak_progress":100,"struggling":False,"user": url}
        self.client.put(exerciselog_url, data=json.dumps(data), headers=headers)
        self.client.get("/api/exerciselog/?exercise_id=addition_1&user=" + user_id)
        self.client.get("/api/attemptlog/?user=" + user_id + "&limit=10&exercise_id=addition_1&context_type__in=playlist&context_type__in=exercise")


    @task(4)
    def load_exercise(self):
        # self.static()
        # self.exercise_static()
        response = self.client.get("/securesync/api/user/status")
        user_id = json.loads(response.text)["user_id"]
        # self.client.get("/static/khan-exercises/third_party/MathJax/2.1/config/KAthJax-da9a7f53e588f3837b045a600e1dc439.js")
        # self.client.get("/static/khan-exercises/exercises/prime_numbers.html")
        # self.client.get("/math/arithmetic/factors-multiples/prime_numbers/e/prime_numbers/")
        self.client.get("/api/exercise/prime_numbers")
        self.client.get("/api/exerciselog/?exercise_id=prime_numbers&user=" + user_id)
        self.client.get("/api/attemptlog/?user=" + user_id + "&limit=10&exercise_id=prime_numbers&context_type__in=playlist&context_type__in=exercise")

    @task(5)
    def answer_exercise(self):
        response = self.client.get("/securesync/api/user/status")
        user_id = json.loads(response.text)["user_id"]
        exerciselog_id = binascii.b2a_hex(os.urandom(15))
        exerciselog_url = "/api/exerciselog/" + exerciselog_id + "/"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        url  = "/securesync/api/user/" + user_id + "/"
        data = {"exercise_id":"prime_numbers","user":url,"streak_progress":20,"points":28,"attempts":1,"complete":False}
        self.client.post("/api/exerciselog/", data=json.dumps(data), headers=headers)
        data = {"exercise_id":"prime_numbers","user":url ,"context_type":"exercise","context_id":"","language":"","version":"0.13.0","seed":17,"complete":True,"points":28,"response_count":1,"response_log":"[{\"type\":\"loaded\",\"timestamp\":\"2015-04-21T12:38:19.189\"},{\"type\":\"answer\",\"answer\":{\"value\":\"<code><script type=\\\"math/tex\\\">31</script></code>\",\"index\":1},\"correct\":true,\"timestamp\":\"2015-04-21T12:38:30.374\"}]","timestamp":"2015-04-21T12:38:19.189","correct":True,"answer_given":{"value":"<code><script type=\"math/tex\">31</script></code>","index":1},"time_taken":11186}
        self.client.post("/api/attemptlog/", data=json.dumps(data), headers=headers)
        data = {"attempts":5,"attempts_before_completion":5,"complete":True,"completion_counter":None,"completion_timestamp":"2015-04-10T13:35:39.940","counter":None,"deleted":False,"exercise_id":"addition_1","id":exerciselog_id,"language":None,"points":100,"resource_uri": exerciselog_url,"signature":None,"signed_version":1,"streak_progress":100,"struggling":False,"user": url}
        self.client.put(exerciselog_url, data=json.dumps(data), headers=headers)
        self.client.get("/api/exerciselog/?exercise_id=addition_1&user=" + user_id)
        self.client.get("/api/attemptlog/?user=" + user_id + "&limit=10&exercise_id=addition_1&context_type__in=playlist&context_type__in=exercise")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000
