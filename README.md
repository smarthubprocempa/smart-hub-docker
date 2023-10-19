# Webservice to detect skin cancer
This project is a Python WS which evaluates the probability of cancer based upon an image of a skin lesion. 

For evaluation call 
POST host:port/skincancer/api/check 
Form-data with binary parameter named "file"

The docker image can be built using the Docker file included into this repository.
To run the image it is necessary to expose port 5000, the one used to reach the WS. 


