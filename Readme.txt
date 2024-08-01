Create a virtual environment
----------------------------
python -m venv venv

To Activate the environment
---------------------------
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install required packages
-------------------------
pip3 install fastapi uvicorn pymongo pydantic


To Test the CRUD operations
Create User     :   POST /api/users
Get All Users   :   GET /api/users
Get User by ID  :   GET /api/users/{user_id}
Update User     :   PUT /api/users/{user_id}
Delete User     :   DELETE /api/users/{user_id}