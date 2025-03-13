# Frogss API

Frogss is a task management API inspired by Brian Tracy's *Eat That Frog!* methodology, helping users prioritize and complete their most challenging tasks first.

## Features
- **User Authentication & Authorization** (JWT-based authentication)
- **Task Management** (Create, Read, Update, Delete frogs)
- **Priority-Based Organization**
- **Frog Status Tracking**
- **Due Date Assignment**

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- FastAPI
- Uvicorn
- MongoDB (or a configured database connection)

### Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd frogss_API
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add your configurations (e.g., database URL, secret keys).

4. Start the API server:
   ```bash
   uvicorn app.server.app:app --reload
   ```

## API Documentation
Frogss API includes interactive API documentation.

- **Swagger UI:** Visit `http://127.0.0.1:8000/docs/` after running the server.

## Usage

### Authentication
- Click the Authorize 🔒 button in Swagger UI
- Enter username and password (pa$$word1)

For a list of endpoints, refer to `/docs/`.

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Submit a pull request

## License
MIT License

