# Project: Perfect Capping App for WoW
## Author: Bethany Van Meter, bethanyv21@gmail.com
This base code is taken from example projects for CIS 322 at UO by Professor Ramakrishnan Durairajan 

## To run:

Ensure credentials.ini is in the brevets folder.

* `cd perfect_capping/`
* `./run.sh`

run.sh takes care of building the docker container and running it. The docker container will be running on whatever port number you decide in credentials.ini. In my case, I chose port 5000 in my credentials file, so I can go to:

`localhost:5000`

in my browser, I will see my running application (if running locally).
