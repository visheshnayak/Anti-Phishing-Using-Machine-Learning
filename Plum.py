import multiprocessing
from analysis import urlAnalysis
from server import startServer

analysis = multiprocessing.Process(name = 'analysis', target = urlAnalysis)
server = multiprocessing.Process(name = 'server', target = startServer)

server.start()
analysis.start()
