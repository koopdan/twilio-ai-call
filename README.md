Setup Instructions:

Clone the Repository  

bash-

git clone https://github.com/YOUR_GITHUB_USERNAME/twilio-ai-call.git

cd twilio-ai-call


Backend Setup (FastAPI):

Install Dependencies  

Make sure you have Python 3.10+ installed. Then, run:

bash-

cd backend

pip install -r requirements.txt

(Set Up Environment Variables)

Create a `.env` file inside `backend/` and add:

TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
DEEPGRAM_API_KEY=your_deepgram_api_key

(Run the Backend)

bash-

uvicorn main:app --reload --host 0.0.0.0 --port 8000

By default, the API will run on http://localhost:8000


Frontend Setup (React):

Install Dependencies  

Ensure Node.js 16+ is installed. Then, run:

bash-

cd frontend

npm install

Run the Frontend  

bash-

npm start

This will start the frontend on http://localhost:3000

