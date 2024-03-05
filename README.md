# Django Chat App

![Django Version](https://img.shields.io/badge/django-v3.2-blue.svg)
![Python Version](https://img.shields.io/badge/python-v3.9-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple chat application built with Django, allowing users to communicate in real-time.

## Features

- **Real-time Messaging**: Users can send and receive messages instantly.
- **User Authentication**: Users can register, login, and logout securely.
- **Message History**: View past messages in the chatroom.
- **User Presence**: See who else is online.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Rahulns21/chat-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-django-chat-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://localhost:8000` in your web browser.

## Usage

1. Register for an account or login if you already have one.
2. Once logged in, you will be redirected to the chatroom.
3. Start sending messages and enjoy chatting with other users in real-time!

## Technologies Used

- **Django**: Python web framework for building the application.
- **Django Channels**: Provides WebSockets support for real-time communication.
- **HTML/CSS**: Frontend styling and structure.
- **JavaScript**: Used for frontend interactivity and real-time messaging.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
