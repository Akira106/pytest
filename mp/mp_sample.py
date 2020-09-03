import multiprocessing as mp


class MPsample():

    def __init__(self, web_api):
        self.web_api = web_api
        self.q = mp.Queue()

    def start(self):
        self.pobj = mp.Process(target=self.func, args=(self.web_api, self.q))
        self.pobj.start()

    def stop(self):
        self.pobj.join()

    def func(self, web_api, q):

        value = web_api.get_value()
        q.put(value)

    def get_queue(self):
        return self.q
