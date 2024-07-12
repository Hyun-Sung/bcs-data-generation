This script is to generate a data file with generated data for the projects collecion to upload to mongodb. 

the project was made with the following versions of the dependencies
faker 25.8.0
dnspython 2.6.1
pip 24.0
pymongo 4.7.3
python-dateutil 2.9.0.post0
six 1.16.0

A config.json file will need to be configured. An example one is included 

notes:
the projects documents have a different unique way of doing document ids that requires a binary conversion.
date types need a bsondate time which is handled by the mongotype data function in the datageneration script