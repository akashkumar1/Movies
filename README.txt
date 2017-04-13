***Steps for setup***
1. create virtualenv
2. Activate virtualenv by running 'source path/to/virtualenv/bin/activate'
3. run 'pip install -r requirements.txt' to install requirements in your virtualenv
4. run 'python manage.py migrate' to reflect migrations
5. run 'python manage.py runserver' to run the project on local machine.
6. visit 'http://127.0.0.1:8000/scrape' and wait for some time. This step is required as it reads the datasf api and 
enters distinct enteries into db.(wait for sometime)
or
schedule a cron to run scrape method in views.py file to regularly do this job.
7. run 'python manage.py createsuperuser' and fill required details
8. Now, visit 'http://127.0.0.1:8000/admin/web/movie/' to see the data of your db(you can perform CRUD on any entry in db from here). 
9. visit 'http://127.0.0.1:8000/home' to see the homepage consisting of movie list along with other attributes
10. visit 'http://127.0.0.1:8000/api/movies/' to see api's
11. you can apply filter's on any attribute:
	for e.g.:  visit 'http://127.0.0.1:8000/api/movies/?production=SPI%20Cinemas' and  see the results
12. run 'tail -f tmp/server_movies.log' to see log's.
13. before deploying on main server run 'python manage.py test' to check if code passes unit-testcases, if 
it does you can deploy else please contact me.


***Additional Information about project***
1. Api's are paginated, pagesize=10
2. After visiting home page user can user 'next' and 'previous' links to get relevant paginated response.
3. title and director have unique together contraint on them to avoid duplicates during scraping.

 