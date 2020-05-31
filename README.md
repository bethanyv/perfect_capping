# Project: Perfect Capping App for WoW
## Author: Bethany Van Meter, bethanyv21@gmail.com

## To run:

Ensure credentials.ini is in the brevets folder.

* `cd brevets/`
* `./run.sh`

run.sh takes care of building the docker container and running it. The docker container will be running on whatever port number you decide in credentials.ini. In my case, I chose port 6021 in my credentials file, so I can go to:

localhost:6021

in my browser, I will see my running application (if running locally).

## To run the nosetests
You will have to ssh into the running docker container by:

* `docker exec -it <container name> nosetests tests/test_acp_times.py`

To get the docker container name, run `docker ps` and see what the container name is.

## The Calculator Rules:

Rules are based on the table below:

| Control location (km) | Minimum Speed (km/hr) | Maximum Speed (km/hr)  |
| --------------------- | --------------------- | ---------------------- |
| 0 - 200               | 15                    | 34                     |
| 200 - 400             | 15                    | 32                     |
| 400 - 600             | 15                    | 30                     |
| 600 - 1000            | 11.428                | 28                     |
| 1000 - 1300           | 13.333                | 26                     |

The calculation of a control's opening time is based on the maximum speed. Calculation of a control's closing time is based on the minimum speed.

* If a brevet equal to or below 60km, the close times are determined by 20km/hour plus 1 hour.
* If a control location distance is greater than the brevet, the brevet distance will be used to calculate the open and close times.
* The max closing times for each brevet length are predetermined (in hours and minutes, HH:MM):
	* 13:30 for 200 KM
	* 20:00 for 300 KM
	* 27:00 for 400 KM
	* 40:00 for 600 KM
	* and 75:00 for 1000 KM
		* In this case, if a brevit is 200km, and the control location is 200km, we won't calculate with the normal calculator, but by using the time limit above (so: 13:30 rather than 13:20).
* If a control point of 0 is given (the start), the closing time is 1 hour after the starting time. 
* Control point open and close times are calculated incrementally. For example: a 600km brevet distance with control points 150, 250, 350, 460, and 603 are determined by:
	* 150 -> within bracket 0-200, min speed = 15, max speed = 34
	* 250 -> within bracket 200-400 for 50 km (min speed = 15, max speed = 32), within bracket 0-200 for 200km (min speed = 15, max speed = 34)
	* 350 -> within bracket 200-400 for 150km (min speed = 15, max speed = 32), within bracket 0-200 for 200km (min speed = 15, max speed = 34)
	* 460 -> within bracket 400-600 for 60km (min speed = 15, max speed = 30), within bracket 200-400 for 200km (min speed = 15, max speed = 32), within bracket 0-200 for 200km (min speed = 15, max speed = 34)
	* 603 -> over the brevet length of 600, so calculate close time using max time for 600 and calculate open time using 600: within bracket 400-600 for 200km (min speed = 15, max speed = 30), within bracket 200-400 for 200km (min speed = 15, max speed = 32), within bracket 0-200 for 200km (min speed = 15, max speed = 34)