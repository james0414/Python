class PyObservable(object):
    """
    USAGE:
    def observer_function(param)
        print(param)
    
    subject = Observable()
    subject.registerObserver(observer_function)
    subject.notifyObservers('test')
    """

    def __init__(self):
        self.__observers = []
        self._observers = []

    def registerObserver(self, observer):
        self.__observers.append(observer)

    def notifyObservers(self, param):
        for observer in self.__observers:
            observer(param)

    def attach(self, evtname, observer):
        self._observers.append([evtname, observer])

    def detach(self, evtname, observer):
        if [evtname, observer] in self._observers:
            self._observers.remove([evtname, observer])
    
    def notify(self, evt):
        for evtname, observer in self._observers:
            if evtname == evt.name:
                observer(evt)
