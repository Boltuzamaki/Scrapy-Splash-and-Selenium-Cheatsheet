## Storing data into MongoDB Cloud

- First go to [cloud mongo](https://cloud.mongodb.com/)
- Then Sign in or Sign Up
- Create a new cloud cluster 

Then Install MongoDB in your local 
```
conda install pymongo dnspython -y
```
After cluster is created go to database access
- Create a new user
  
Then go to network access and to allow all IP type
```
0.0.0.0/0
```
Then go to cluster click connect and then connect your application
- Chose driver python
- Then copy the link and paste to the pipeline.py 