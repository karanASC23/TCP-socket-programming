"""
name: karan marwaha
nuid: 002359760


When creating a TCP connection the distinction betweena a UDP connection is the introduction of a welcome socket coined as the connectionSocket. the TCP server will ultiize this "knock" from the client server socket to do the TCP handshake and create a socket for the client and server to transmit data. this connection can be seen as a stable wire connection the clientSocket & severSocket(connection socket NOT welcome socket). After this inital connection is made a while loop is used to split up the elements of the expression flag and send back the evaulation untila SUCC or FAIL flag is read in this response from the TCP server. This script was made in a linux terminal via vim IDE. 

testing: At first, my code wouldn't complie because I spelled AF_INET as AF_NET. After complining I was confused how to run the both the sample server and client server together but I relized I could just open another terminal. Then I ran sample local server first b/cit waits for the "knock."
Then I forgot to put the sampleServer IP and port # when I ran thsi ,py file as the connect method expects a integer and it was a empty string. 
Then I kept entering just my nuid forgetting it must be entered in server format.  
Then I relized there would be more than one expression sent before success or fail falg was raised so i choose to add a while loop until a SUCC or FAIL falg is seen in the response emssage. I choose a while loop because I did not know how many expressions the server would send.
After a while of inputting eval expressions, i realize I needed to automate this. I did some research on how to isolate poarts of a string to evaulate it which i then implmenetated into my while loop. I also added a close connection after I received the flag.
I also then hardcoded my NUID so it would be automated. 
After getting the success flag on the sample server I went to the real server.

sercet flag: 3319b92648a137765bbf88ec71bdfbf65452236db264a635ce093fc2e9a9470a
"""

from socket import *

sampleServerIP = '129.10.33.215'; 
sampleServerWelcomeSocketPortNumber = 12009;


clientSocket = socket(AF_INET, SOCK_STREAM) #AF_NET indicator for network layer running on IPv4 & SOCK_STREAM indicates over TCP

clientSocket.connect((sampleServerIP, sampleServerWelcomeSocketPortNumber));

introductoryMessage = "EECE2540 INTR 002359760";


clientSocket.send(introductoryMessage.encode());

while True:

	expression = clientSocket.recv(1024);

	print(expression.decode());
	
	if "SUCC" in expression.decode() or "FAIL" in expression.decode():
		break
	
	brokenExpression = expression.decode().split() #break up expression based on spaces
	
	if brokenExpression[3] == '+':
		rslt = int(brokenExpression[2]) + int(brokenExpression[4]);
	elif brokenExpression[3] == '-':
		rslt = int(brokenExpression[2]) - int(brokenExpression[4]);
	elif brokenExpression[3] == '*':
		rslt = int(brokenExpression[2]) * int(brokenExpression[4]);
	elif brokenExpression[3] == '/':
		rslt = int(brokenExpression[2]) / int(brokenExpression[4]);

	clientSocket.send(f"EECE2540 RSLT {rslt}".encode());

clientSocket.close()
