# Example client socket programming

__author__ = 'sidmishraw'


from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from sys import exc_info


class Client(object):
  'All client related code goes in here'

  socket_family = AF_INET
  socket_type = SOCK_STREAM

  def __init__(self, server_address = '', server_port = 8085):
    'initializes the client socket'
    self.__cl_socket = socket(self.socket_family, self.socket_type)

    self.__cl_socket.connect((server_address, server_port))

    print('Connected to server at %s:%s' % (server_address, server_port))

  def send(self, input_str):
    'sends the input after wrapping it up as a request'
    request_str = 'GET %s' % str(input_str)

    request = bytes(request_str, encoding = 'utf-8')

    self.__cl_socket.send(request)

  def recv(self, bytes_size = 1024):
    'By default receives just 1024 Bytes'
    bytes_recvd = self.__cl_socket.recv(bytes_size)
    return bytes_recvd
      



def main():
  'main point of entry for the client program'
  cl = Client()

  # send the request
  cl.send('increment?91')

  response = str(cl.recv(4096), encoding = 'utf-8')

  output = response.split('\n')[-1]

  # receive the response(it's in bytes)
  print('incremented to %s' % output)

if __name__ == '__main__':
  main()



  