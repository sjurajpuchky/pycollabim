from pycollabim import Collabim

collabim = Collabim('config.ini')
collabim.authenticate()
activity_data = {'activity_name': 'Activity 1', 'description': 'This is a new activity'}
collabim.activity_create(activity_data)
