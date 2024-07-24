# API Documentation
### Posts Endpoints
1. List All Posts
- URL: /posts/
- Method: GET
- Description: Retrieve a list of all posts.
- Response Example:
    ```sh
    [
        {
            "id": 1,
            "title": "First Post",
            "content": "This is the content of the first post.",
            "date_posted": "2024-07-23T10:00:00Z",
            "author": 1,
            "likes": []
        },
        ...
    ]
    ```

2. Retrieve, Update, or Delete a Specific Post

- URL: /posts/<int:pk>/
- Methods: GET, PUT, DELETE
- Description: Retrieve, update, or delete a specific post by its primary key.
- Response Example (GET):
    ```sh
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the content of the first post.",
        "date_posted": "2024-07-23T10:00:00Z",
        "author": 1,
        "likes": []
    }
    ```

### Users Endpoints
3. List All Users
- URL: /users/
- Method: GET
- Description: Retrieve a list of all users.
- Response Example:
    ```sh
    [
        {
            "id": 1,
            "username": "johndoe",
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com"
        },
        ...
    ]
    ```

4. Retrieve, Update, or Delete a Specific User

- URL: /users/<int:pk>/
- Methods: GET, PUT, PATCH, DELETE
- Description: Retrieve, update, or delete a specific user by their primary key.
- Response Example (GET):
    ```sh
    {
        "id": 1,
        "username": "johndoe",
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com"
    }
    ```

### Profiles Endpoints
5. List All Profiles
- URL: /profiles/
- Method: GET
- Description: Retrieve a list of all profiles.
- Response Example:
    ```sh
    [
        {
            "id": 1,
            "bio": "This is John's bio.",
            "image": "default.png",
            "twitter_link": "https://twitter.com/johndoe",
            "instagram_link": "https://instagram.com/johndoe",
            "linkedin_link": "",
            "telegram_link": "https://telegram.com/johndoe",
            "user": 5, 
            "follows": []
        },
        ...
    ]
    ```

6. Retrieve, Update, or Delete a Specific Profile
- URL: /profiles/<int:pk>/
- Methods: GET, PUT, PATCH, DELETE
- Description: Retrieve, update, or delete a specific profile by its primary key.
- Response Example (GET):
    ```sh
    {
        "id": 1,
        "bio": "This is John's bio.",
        "image": "default.png",
        "twitter_link": "https://twitter.com/johndoe",
        "instagram_link": "https://instagram.com/johndoe",
        "linkedin_link": "",
        "telegram_link": "https://telegram.com/johndoe",
        "user": 5, 
        "follows": []
    }
    ```

7. List Followers of a Specific Profile
- URL: /profiles/<int:pk>/followers/
- Method: GET
- Description: Retrieve a list of users who follow a specific profile.
- Response Example:
    ```sh
    [
        {
            "id": 3,
            "bio": "",
            "image": "http://127.0.0.1:8000/media/profile_pics/Lion-icon.png",
            "twitter_link": "https://twitter.com",
            "instagram_link": "https://instagram.com",
            "linkedin_link": "",
            "telegram_link": "https://telegram.com",
            "user": 5,
            "follows": [
                1,
                4
            ]
        }
        ...
    ]
    ```

8. List Following Profiles of a Specific Profile

- URL: /profiles/<int:pk>/following/
- Method: GET
- Description: Retrieve a list of profiles that a specific profile is following.
- Response Example:
    ```sh
    [
        {
            "id": 3,
            "bio": "",
            "image": "http://127.0.0.1:8000/media/profile_pics/Lion-icon.png",
            "twitter_link": "https://twitter.com",
            "instagram_link": "https://instagram.com",
            "linkedin_link": "",
            "telegram_link": "https://telegram.com",
            "user": 5,
            "follows": [
                1,
                4
            ]
        }
        ...
    ]
    ```
