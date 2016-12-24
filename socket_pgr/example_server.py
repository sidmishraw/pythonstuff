# Example server socket programming

__author__ = 'sidmishraw'

from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from sys import exc_info



class Server(object):
  'All server related code goes in here'
  
  socket_family = AF_INET
  socket_type = SOCK_STREAM

  def __init__(self, server_address = '', server_port = 8085, nbr_requests = 5):
    'initializes the server socket and bind to default 127.0.0.1:8085, default \
    request queue size = 5'

    self.__sv_address = server_address
    self.__sv_port = server_port

    self.__sv_socket = socket(self.socket_family, self.socket_type)
    self.__sv_socket.bind((self.__sv_address, self.__sv_port))
    self.__sv_socket.listen(nbr_requests)

  def server(self, serving_func):
    'the main loop that runs in the server'

    print('server running at address %s:%s' % (self.__sv_address, self.__sv_port))

    while True:

      client_socket = None

      try:
        # accept the incoming connection
        client_socket, client_address = self.__sv_socket.accept()

        print('serving the client %s having address %s:%s' % (client_socket, \
          client_address[0], client_address[1]))

        # receive the incoming request
        request = client_socket.recv(4096)

        request_type, request_body = str(request, encoding = 'utf-8').split(' ')[0:2]

        print('incoming request type = %s' % request_type)
        print('incoming input string = %s' % request_body)

        output_str = serving_func(request_body)

        response_body = '''\HTTP/1.1 200 OK\n\n%s''' % output_str

        response = bytes(response_body, encoding = 'utf-8')

        client_socket.sendall(response)
      except Exception as e:

        print('Exception occurred', exc_info())
      finally:
        if client_socket != None:
          client_socket.close()




def increment(req_str):
  'just a sample increment function that increments the input nbr'
  inputs = req_str.strip(r'/').split(r'?')

  if inputs[0].lower() != 'increment':
    raise Exception('not a valid request for incrementing')

  arg_1 = int(inputs[1])

  return arg_1 + 1


def main():
  'just the main function acting as the main entry point for the \
  program flow'
  server_1 = Server()
  server_1.server(serving_func = increment)


if __name__ == '__main__':
  main()




  