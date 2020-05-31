# Project: Perfect Capping App for WoW ![alt text](https://github.com/bethanyv/perfect_capping/blob/master/perfect_capping/static/images/small_logo_3.png "Wow Logo")
## Author: Bethany Van Meter, bethanyv21@gmail.com
This system is for finding what rank and level of players (up to 3) that, when killed, will equal the exact honor points the user enters.
A table will display on the page with all possible options for one, two, and three player combinations to reach the desired honor point amount.

This base code is taken from example projects for CIS 322 at UO by Professor Ramakrishnan Durairajan 

## To run:

### If Docker is not installed, install Docker:
[Click here to install Docker for your system](https://docs.docker.com/get-docker/ "Get Docker")

### 1. Clone this repository by going into the terminal/command line and typing:

`git clone https://github.com/bethanyv/perfect_capping.git`

### 2. Pick one of the following:
#### a. File explorer (easiest):

* Go into perfect_capping folder
* Double click on `run.sh`
* Go to `localhost:5000/` in your browser to view the program!

#### b. Terminal/Command line:

Ensure credentials.ini is in the perfect_capping folder.

* `cd perfect_capping/`
* `./run.sh`

run.sh takes care of building the docker container and running it. So I can go to:

`localhost:5000`

in my browser, I will see my running application.
