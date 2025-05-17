🗂️ Project Structure

python-generators-0x00/
├── seed.py                 
├── 0-stream_users.py       
├── 1-batch_processing.py   
├── 2-lazy_paginate.py      
├── user_data.csv           
├── 0-main.py               
├── 1-main.py               
├── 2-main.py               
├── 3-main.py               
└── README.md

⚙️ Setup Instructions
1. Database Setup and Seeding
Create and populate the MySQL database using seed.py.

Table: user_data
Field	Type	Properties
user_id	UUID	Primary Key, Indexed
name	VARCHAR	Not Null
email	VARCHAR	Not Null
age	DECIMAL	Not Null

🧪 Features and Functionalities
1. ✅ Stream Rows One by One
File: 0-stream_users.py
Function: stream_users()

2. 📦 Batch Processing of Large Data
File: 1-batch_processing.py
Functions:

stream_users_in_batches(batch_size)

batch_processing(batch_size)

3. 📄 Lazy Loading with Pagination
File: 2-lazy_paginate.py
Function: lazy_pagination(page_size)

Implements lazy pagination to yield one page of results at a time without loading all data at once.

🧪 Sample Output
Example of streamed data:

json
Copy
Edit
{'user_id': '00cc08cc...', 'name': 'Alma Bechtelar', 'email': 'Shelly_Balistreri22@hotmail.com',}
🛠️ Technologies
- Python 3
- MySQL
- CSV