# blog_application

# Requirements
 * Install the packages in requirements.txt
   ```
   [+] Open Terminal on the root directory and run the following
        [-] pip install -r requirements.txt
    ```
 
# Procedure
 * Fork the Repository [click here](https://github.com/akkupy/School-Management-System/fork)
 * Clone the repository 
 * Run python manage.py runserver.
 * urls info
    1. posts/ : list of all posts
    2. posts/<pk> : retrieve specified post using primary key
     ex. http://127.0.0.1:8000/posts/2
    3. post_update/ : for Creating , Updating, Deleting post 
     here just need to specify the method while calling the api.
     for creating POST method, Updating PATCH and deleting DELETE method.
     and For updating and deleting specify id/primary in body
    4. comments/ : for getting list of all the comments
    5. comments_update/ : for creating new comment.

 
