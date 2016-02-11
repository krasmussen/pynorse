#!/usr/bin/env python
import websocket
from time import sleep

class norse():
    def __init__(self, ws_location='ws://map.norsecorp.com/socketcluster/'):
        self.ws_location = ws_location
        self.ws = websocket.WebSocket()
    def connect(self):
        self.ws.connect(self.ws_location)
        self.ws.send('{"event":"#handshake","data":{"authToken":null},"cid":1}')
        _ = self.ws.recv()
        self.ws.send('{"event":"#subscribe","data":"global","cid":2}')
        sleep(0.5)
    def process_stream(self):
        while True:
            try:
                self.handler(self.ws.recv())
                sleep(0.125)
            except KeyboardInterrupt:
                break
            except:
                self.connect()
    def handler(self, data):
        """Feel free to override this method to handle processing of the data however you want"""
        print(data)

if __name__ == '__main__':
    print('starting app')
    n = norse()
    print('starting datastream press Ctrl + C to stop stream')
    n.process_stream()
    print('stopping app')

