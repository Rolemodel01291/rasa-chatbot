## happy path
* greet
	- utter_greet
* mood_great
	- utter_happy
* get_garan
	- utter_get_garan

## sad path 1
* greet
	- utter_greet
* mood_unhappy
	- utter_cheer_up
	- utter_did_that_help
* get_garan
	- utter_get_garan
* mood_affirm
	- utter_happy

## sad path 2
* greet
	- utter_greet
* mood_unhappy
	- utter_cheer_up
	- utter_did_that_help
* get_garan
	- utter_get_garan
* mood_deny
	- utter_goodbye

## say goodbye
* goodbye
	- utter_goodbye
