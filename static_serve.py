import os
import subprocess
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RootResource(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.putChild(b'static', File("static"))

root = RootResource()
factory = Site(root)
reactor.listenTCP(8080, factory)

class FileChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        print("File changed:", event.src_path)
        reactor.callFromThread(restart_server)

def restart_server():
    os.execv(sys.executable, ['python'] + sys.argv)

observer = Observer()
observer.schedule(FileChangeHandler(), path='.', recursive=True)
observer.start()

reactor.run()
