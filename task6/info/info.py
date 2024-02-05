APIs = {
    "APIs": [
        {
            "request_link": "'/' (GET)",
            "purpose": "Shows all endpoints and link to the user list",
            "example": "N/A",
        },
        {
            "request_link": "'/app/users/profile/:name' (GET)",
            "purpose": "Shows specific user's profile",
            "example": "/app/users/profile/Bob",
        },
        {
            "request_link": "'/app/users' (GET)",
            "purpose": "Shows all users and link to their profile",
            "example": "N/A",
        },
        {
            "request_link": "'/app/image' (GET)",
            "purpose": "Shows image",
            "example": "N/A",
        },
        {
            "request_link": "'/app/users/add/' (POST)",
            "purpose": "Adds new user to the user list",
            "example": """
                {
                    "name": "NewUser",
                    "lastname": "NewLastName",
                    "email": "newuser@a.com"
                }
            """,
        },
        {
            "request_link": "'/app/users/delete/:name' (DELETE)",
            "purpose": "Deletes specific user",
            "example": "/app/users/delete/NewUser",
        },
    ]
}
